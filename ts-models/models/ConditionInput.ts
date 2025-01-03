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

import { CommentAnnotation } from '../models/CommentAnnotation';


export class ConditionInput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'text': string;
    'dictionaryId'?: string | null;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': ConditionInputInstanceTypeEnum;
    'contextIds'?: Array<string | null>;
    'appliesToIds'?: Array<string | null>;

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
            "name": "text",
            "baseName": "text",
            "type": "string",
            "format": ""
        },
        {
            "name": "dictionaryId",
            "baseName": "dictionaryId",
            "type": "string",
            "format": ""
        },
        {
            "name": "notes",
            "baseName": "notes",
            "type": "Array<CommentAnnotation>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "ConditionInputInstanceTypeEnum",
            "format": ""
        },
        {
            "name": "contextIds",
            "baseName": "contextIds",
            "type": "Array<string | null>",
            "format": ""
        },
        {
            "name": "appliesToIds",
            "baseName": "appliesToIds",
            "type": "Array<string | null>",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ConditionInput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum ConditionInputInstanceTypeEnum {
    Condition = 'Condition'
}
