# **Converting USDM YAML to OpenAPI Specification**
This script is designed to parse a USDM-compliant YAML file, convert it into a valid OpenAPI 3.0 specification, and save the resulting OpenAPI YAML to a file. Below are the instructions for its usage.
## **Requirements**
Ensure that you have the following installed:
1. **Node.js and npm**:
    - Download and install [Node.js](https://nodejs.org/).

2. **Dependencies**:
    - Install the necessary npm packages using the following command in the project directory:
``` bash
     npm install js-yaml ts-node
```
## **Steps to Use**
### 1. Prepare Input File
- Place the USDM YAML file you want to convert in the `dataStructure.yml` file at the appropriate directory (as mentioned in the `filePath` in the script).
- Example `dataStructure.yml` structure:
``` yaml
   Address:
     NCI C-Code: C42610
     Definition: "A description of the address."
     Preferred Term: "Address"
     Attributes:
       Street:
         Type: ["#/string"]
         "Cardinality": "1..1"
       City:
         Type: ["#/string"]
         "Cardinality": "1..1"
```
### 2. Run the Script
- Execute the script using the following command:
``` bash
  ts-node yaml2OpenApiGenerator.ts
```
- If successful, the generated OpenAPI file will be saved in the same directory as `USDM-Model_openapi.yaml`.

### 3. Output
#### Output File
The script generates an `OpenAPI` YAML file. This file contains:
- **OpenAPI Metadata** (e.g., title, version).
- **Schemas**: Mapped from the USDM YAML.

Example Generated File (`USDM-Model_openapi.yaml`):
``` yaml
openapi: 3.0.3
info:
  title: USDM to OpenAPI
  version: 1.0.0
paths: {}
components:
  schemas:
    Address:
      type: object
      description: |
        NCI C-Code: C42610
        Definition: A description of the address.
        Preferred Term: Address
      properties:
        Street:
          type: string
        City:
          type: string
      required:
        - Street
        - City
```
## **Error Handling**
The script will log warnings and continue processing even if:
1. Invalid or missing fields are found in the YAML.
2. An unsupported `Type` or malformed attribute is detected.

If the script fails entirely, an error message will be printed on the console:
``` bash
Error loading or parsing YAML: [error details]
```
## **Customization**
You can adapt the script for your specific needs:
1. Modify `mapProperty` to handle more data types or relationships.
2. Change the `info` section in `generateOpenApiFromUsdm()` for custom metadata (e.g., title, version).

## **Debugging**
If you’d like to inspect the intermediate objects (such as `USDM` or individual schemas), you can insert `console.log` lines or use `util.inspect`:
``` typescript
import { inspect } from 'util';
console.log(inspect(openApiDoc, { depth: null, colors: true }));
```
## **FAQs**
### **What is the purpose of the script?**
It converts USDM-compliant YAML into an OpenAPI specification for use in API documentation, testing, and development.
### **Can I add additional attributes to the OpenAPI schema?**
Yes, you can customize the `convertUsdmClassToSchema` function to include additional fields or metadata by modifying how attributes are processed and mapped.
### **What happens if the input YAML is invalid?**
The script logs warnings or errors, depending on the severity, and tries to process as much of the data as possible. Ensure your YAML is properly formatted.
Feel free to reach out with any additional questions!
