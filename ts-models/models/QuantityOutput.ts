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

import { AliasCode } from '../models/AliasCode';


export class QuantityOutput {
    'id': string;
    'value': number;
    'unit'?: AliasCode | null;
    'instanceType': QuantityOutputInstanceTypeEnum;

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
            "name": "value",
            "baseName": "value",
            "type": "number",
            "format": ""
        },
        {
            "name": "unit",
            "baseName": "unit",
            "type": "AliasCode",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "QuantityOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return QuantityOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum QuantityOutputInstanceTypeEnum {
    Quantity = 'Quantity'
}

