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

import { ParameterMap } from '../models/ParameterMap';


export class SyntaxTemplateDictionary {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'parameterMaps': Array<ParameterMap>;
    'instanceType': SyntaxTemplateDictionaryInstanceTypeEnum;

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
            "name": "parameterMaps",
            "baseName": "parameterMaps",
            "type": "Array<ParameterMap>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "SyntaxTemplateDictionaryInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return SyntaxTemplateDictionary.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum SyntaxTemplateDictionaryInstanceTypeEnum {
    SyntaxTemplateDictionary = 'SyntaxTemplateDictionary'
}

