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


export class StudyAmendmentImpactOutput {
    'id': string;
    'type': Code;
    'text': string;
    'isSubstantial': boolean;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': StudyAmendmentImpactOutputInstanceTypeEnum;

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
            "name": "type",
            "baseName": "type",
            "type": "Code",
            "format": ""
        },
        {
            "name": "text",
            "baseName": "text",
            "type": "string",
            "format": ""
        },
        {
            "name": "isSubstantial",
            "baseName": "isSubstantial",
            "type": "boolean",
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
            "type": "StudyAmendmentImpactOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return StudyAmendmentImpactOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum StudyAmendmentImpactOutputInstanceTypeEnum {
    StudyAmendmentImpact = 'StudyAmendmentImpact'
}
