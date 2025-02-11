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

import { Numerator1 } from '../models/Numerator1';
import { QuantityOutput } from '../models/QuantityOutput';


export class StrengthOutput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'denominator'?: QuantityOutput | null;
    'numerator'?: Numerator1 | null;
    'instanceType': StrengthOutputInstanceTypeEnum;

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
            "name": "denominator",
            "baseName": "denominator",
            "type": "QuantityOutput",
            "format": ""
        },
        {
            "name": "numerator",
            "baseName": "numerator",
            "type": "Numerator1",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "StrengthOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return StrengthOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum StrengthOutputInstanceTypeEnum {
    Strength = 'Strength'
}

