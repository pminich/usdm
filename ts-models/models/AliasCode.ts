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


export class AliasCode {
    'id': string;
    'standardCode': Code;
    'standardCodeAliases'?: Array<Code>;
    'instanceType': AliasCodeInstanceTypeEnum;

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
            "name": "standardCode",
            "baseName": "standardCode",
            "type": "Code",
            "format": ""
        },
        {
            "name": "standardCodeAliases",
            "baseName": "standardCodeAliases",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "AliasCodeInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return AliasCode.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum AliasCodeInstanceTypeEnum {
    AliasCode = 'AliasCode'
}
