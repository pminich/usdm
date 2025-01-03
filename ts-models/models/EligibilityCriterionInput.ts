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
import { CommentAnnotation } from '../models/CommentAnnotation';


export class EligibilityCriterionInput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'text': string;
    'dictionaryId'?: string | null;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': EligibilityCriterionInputInstanceTypeEnum;
    'category': Code;
    'identifier': string;
    'nextId'?: string | null;
    'previousId'?: string | null;

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
            "type": "EligibilityCriterionInputInstanceTypeEnum",
            "format": ""
        },
        {
            "name": "category",
            "baseName": "category",
            "type": "Code",
            "format": ""
        },
        {
            "name": "identifier",
            "baseName": "identifier",
            "type": "string",
            "format": ""
        },
        {
            "name": "nextId",
            "baseName": "nextId",
            "type": "string",
            "format": ""
        },
        {
            "name": "previousId",
            "baseName": "previousId",
            "type": "string",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return EligibilityCriterionInput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum EligibilityCriterionInputInstanceTypeEnum {
    EligibilityCriterion = 'EligibilityCriterion'
}
