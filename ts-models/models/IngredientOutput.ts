/**
 * DDF USDM API
 * A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.
 *
 * OpenAPI spec version: 3.10.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { Code } from '../models/Code';
import { SubstanceOutput } from '../models/SubstanceOutput';


export class IngredientOutput {
    'id': string;
    'role': Code;
    'substance': SubstanceOutput;
    'instanceType': IngredientOutputInstanceTypeEnum;

    static readonly discriminator: string | undefined = undefined;

    static readonly mapping: {[index: string]: string} | undefined = undefined;

    static readonly attributeTypeMap: Array<{name: string, baseName: string, type: string, format: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string",
            "format": ""
        },
        {
            "name": "role",
            "baseName": "role",
            "type": "Code",
            "format": ""
        },
        {
            "name": "substance",
            "baseName": "substance",
            "type": "SubstanceOutput",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "IngredientOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return IngredientOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum IngredientOutputInstanceTypeEnum {
    Ingredient = 'Ingredient'
}
