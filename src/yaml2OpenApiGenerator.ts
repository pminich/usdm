#!/usr/bin/env ts-node
import * as fs from 'fs';
import * as path from 'path';
import * as yaml from 'js-yaml';

/**
 * Minimal shape of each USDM “class” in your YAML.
 * (We’re not enumerating every possible field.)
 */
interface UsdmClassDef {
  [key: string]: any;
  Attributes?: {
    [attrKey: string]: {
      Type?: string[];                // E.g. [ '$ref: \'#/string\'' ]
      "Relationship Type"?: string;   // E.g. "Value" or "Ref"
      "Cardinality"?: string;         // E.g. "0..*", "1..1", etc.
      "Model Name"?: string;          // E.g. "id", "notes"
    };
  };
}

/**
 * The top-level structure after parsing your USDM YAML.
 */
type UsdmYaml = Record<string, UsdmClassDef>;

/**
 * The final shape of an OpenAPI 3.0 definition with schemas.
 */
interface OpenApiDoc {
  openapi: string;
  info: {
    title: string;
    version: string;
  };
  paths: Record<string, unknown>;
  components: {
    schemas: Record<string, any>;
  };
}

/**
 * Utility function to check if a type string refers to a primitive OpenAPI type.
 */
function isPrimitiveRef(typeString: unknown): boolean {
  if (typeof typeString !== "string") {
    return false; // Non-string inputs are ignored
  }
  const lowerString = typeString.toLowerCase();
  return ['#/string', '#/boolean', '#/float', '#/date'].some(primitive =>
      lowerString.includes(primitive)
  );
}

/**
 * Converts USDM Relationship Type and Cardinality to an OpenAPI property shape.
 */
function mapProperty(attrKey: string, attrVal: any): { propName: string; finalSchema: any; min: string; max: string } {
  if (!attrVal || typeof attrVal !== "object") {
    throw new Error(`Invalid attribute value for key "${attrKey}". Expected an object but got: ${JSON.stringify(attrVal)}`);
  }

  const relationshipType = attrVal["Relationship Type"] || "Value";
  const cardinality = attrVal["Cardinality"] || "1..1"; // Default to single required
  const propName = attrVal["Model Name"] || attrKey;

  // Ensure `Type` is an array and take the first element
  const rawType = Array.isArray(attrVal.Type) && typeof attrVal.Type[0] === "string" ? attrVal.Type[0] : "";

  let finalSchema: any = {};

  // Determine if the property is a reference to a primitive or another class
  if (isPrimitiveRef(rawType)) {
    finalSchema.type = rawType.includes("Boolean")
        ? "boolean"
        : rawType.includes("Float")
            ? "number"
            : "string";
  } else if (rawType.startsWith("#/")) {
    const referencedName = rawType.slice(2); // Remove the "#/" prefix
    finalSchema.$ref = `#/components/schemas/${referencedName}`;
  } else {
    finalSchema.type = "string"; // Default if type is unknown
  }

  // Handle cardinality (e.g., "0..1", "1..*", etc.)
  const [minStr, maxStr] = cardinality.split("..").map(s => s.trim());
  const min = minStr || "0";
  const max = maxStr || "1";

  if (max === "*") {
    finalSchema = {
      type: "array",
      items: finalSchema,
    };
  }

  return { propName, finalSchema, min, max };
}

/**
 * Converts a single USDM class definition into an OpenAPI schema.
 */
function convertUsdmClassToSchema(className: string, classDef: UsdmClassDef) {
  if (!classDef || typeof classDef !== "object") {
    throw new Error(`Invalid USDM class definition for "${className}". Expected an object.`);
  }

  const descriptionLines: string[] = [];
  if (typeof classDef["NCI C-Code"] === "string") {
    descriptionLines.push(`NCI C-Code: ${classDef["NCI C-Code"]}`);
  }
  if (typeof classDef["Definition"] === "string") {
    descriptionLines.push(`Definition: ${classDef["Definition"]}`);
  }
  if (typeof classDef["Preferred Term"] === "string") {
    descriptionLines.push(`Preferred Term: ${classDef["Preferred Term"]}`);
  }

  const schema: any = {
    type: "object",
    description: descriptionLines.join("\n"),
    properties: {},
    required: [],
  };

  const attributes = classDef.Attributes || {};
  if (typeof attributes === "object" && !Array.isArray(attributes)) {
    for (const attrKey of Object.keys(attributes)) {
      const attrVal = attributes[attrKey];
      try {
        const { propName, finalSchema, min, max } = mapProperty(attrKey, attrVal);

        schema.properties[propName] = finalSchema;

        // Add to "required" if min=1
        if (min === "1") {
          schema.required.push(propName);
        }
      } catch (err) {
        console.warn(`Failed to process attribute "${attrKey}" in "${className}":`, err);
      }
    }
  }

  // Remove "required" if empty
  if (schema.required.length === 0) {
    delete schema.required;
  }

  return schema;
}

/**
 * Converts an entire USDM YAML structure into an OpenAPI document.
 */
function generateOpenApiFromUsdm(usdmData: UsdmYaml): OpenApiDoc {
  if (!usdmData || typeof usdmData !== "object") {
    throw new Error(`Invalid USDM YAML data. Expected an object but got: ${JSON.stringify(usdmData)}`);
  }

  const openApi: OpenApiDoc = {
    openapi: "3.0.3",
    info: {
      title: "USDM to OpenAPI",
      version: "1.0.0",
    },
    paths: {},
    components: {
      schemas: {},
    },
  };

  for (const className of Object.keys(usdmData)) {
    try {
      const classDef = usdmData[className];
      openApi.components.schemas[className] = convertUsdmClassToSchema(className, classDef);
    } catch (err) {
      console.warn(`Failed to process class "${className}":`, err);
    }
  }

  return openApi;
}

// --------------------------------------------------------------------------
// Main Execution: Parse YAML, Convert, Write to OpenAPI
// --------------------------------------------------------------------------
const filePath = path.join(__dirname, "../dataStructure.yml");
const rawYaml = fs.readFileSync(filePath, "utf8");
const parsedUsdm = yaml.load(rawYaml) as UsdmYaml;

try {
  const openApiDoc = generateOpenApiFromUsdm(parsedUsdm);
  const openApiYaml = yaml.dump(openApiDoc, { sortKeys: false });
  fs.writeFileSync(path.join(__dirname, "USDM-Model_openapi.yaml"), openApiYaml);
  console.log("OpenAPI schema generated at openapi.yaml");
} catch (err) {
  console.error("Failed to generate OpenAPI schema:", err);
}