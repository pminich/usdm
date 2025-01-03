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


export class ResponseCode {
    'id': string;
    'isEnabled': boolean;
    'code': Code;
    'instanceType': ResponseCodeInstanceTypeEnum;

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
            "name": "isEnabled",
            "baseName": "isEnabled",
            "type": "boolean",
            "format": ""
        },
        {
            "name": "code",
            "baseName": "code",
            "type": "Code",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "ResponseCodeInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ResponseCode.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum ResponseCodeInstanceTypeEnum {
    ResponseCode = 'ResponseCode'
}

