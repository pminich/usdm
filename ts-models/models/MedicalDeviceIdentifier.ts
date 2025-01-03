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


export class MedicalDeviceIdentifier {
    'id': string;
    'text': string;
    'scopeId': string;
    'instanceType': MedicalDeviceIdentifierInstanceTypeEnum;
    'type': Code;

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
            "name": "text",
            "baseName": "text",
            "type": "string",
            "format": ""
        },
        {
            "name": "scopeId",
            "baseName": "scopeId",
            "type": "string",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "MedicalDeviceIdentifierInstanceTypeEnum",
            "format": ""
        },
        {
            "name": "type",
            "baseName": "type",
            "type": "Code",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return MedicalDeviceIdentifier.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum MedicalDeviceIdentifierInstanceTypeEnum {
    MedicalDeviceIdentifier = 'MedicalDeviceIdentifier'
}

