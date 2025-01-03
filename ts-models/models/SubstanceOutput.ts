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
import { StrengthOutput } from '../models/StrengthOutput';


export class SubstanceOutput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'codes'?: Array<Code>;
    'strengths': Array<StrengthOutput>;
    'referenceSubstance'?: SubstanceOutput | null;
    'instanceType': SubstanceOutputInstanceTypeEnum;

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
            "name": "name",
            "baseName": "name",
            "type": "string",
            "format": ""
        },
        {
            "name": "label",
            "baseName": "label",
            "type": "string",
            "format": ""
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string",
            "format": ""
        },
        {
            "name": "codes",
            "baseName": "codes",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "strengths",
            "baseName": "strengths",
            "type": "Array<StrengthOutput>",
            "format": ""
        },
        {
            "name": "referenceSubstance",
            "baseName": "referenceSubstance",
            "type": "SubstanceOutput",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "SubstanceOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return SubstanceOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum SubstanceOutputInstanceTypeEnum {
    Substance = 'Substance'
}

