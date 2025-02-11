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
import { QuantityOutput } from '../models/QuantityOutput';


export class AdministrableProductPropertyOutput {
    'id': string;
    'name': string;
    'text': string;
    'type': Code;
    'quantity': QuantityOutput;
    'instanceType': AdministrableProductPropertyOutputInstanceTypeEnum;

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
            "name": "text",
            "baseName": "text",
            "type": "string",
            "format": ""
        },
        {
            "name": "type",
            "baseName": "type",
            "type": "Code",
            "format": ""
        },
        {
            "name": "quantity",
            "baseName": "quantity",
            "type": "QuantityOutput",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "AdministrableProductPropertyOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return AdministrableProductPropertyOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum AdministrableProductPropertyOutputInstanceTypeEnum {
    AdministrableProductProperty = 'AdministrableProductProperty'
}

