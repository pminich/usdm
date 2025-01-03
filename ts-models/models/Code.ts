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



export class Code {
    'id': string;
    'code': string;
    'codeSystem': string;
    'codeSystemVersion': string;
    'decode': string;
    'instanceType': CodeInstanceTypeEnum;

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
            "name": "code",
            "baseName": "code",
            "type": "string",
            "format": ""
        },
        {
            "name": "codeSystem",
            "baseName": "codeSystem",
            "type": "string",
            "format": ""
        },
        {
            "name": "codeSystemVersion",
            "baseName": "codeSystemVersion",
            "type": "string",
            "format": ""
        },
        {
            "name": "decode",
            "baseName": "decode",
            "type": "string",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "CodeInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return Code.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum CodeInstanceTypeEnum {
    Code = 'Code'
}

