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
import { ProcedureInput } from '../models/ProcedureInput';


export class ActivityInput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'previousId'?: string | null;
    'nextId'?: string | null;
    'childIds'?: Array<string | null>;
    'definedProcedures'?: Array<ProcedureInput>;
    'biomedicalConceptIds'?: Array<string | null>;
    'bcCategoryIds'?: Array<string | null>;
    'bcSurrogateIds'?: Array<string | null>;
    'timelineId'?: string | null;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': ActivityInputInstanceTypeEnum;

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
            "name": "previousId",
            "baseName": "previousId",
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
            "name": "childIds",
            "baseName": "childIds",
            "type": "Array<string | null>",
            "format": ""
        },
        {
            "name": "definedProcedures",
            "baseName": "definedProcedures",
            "type": "Array<ProcedureInput>",
            "format": ""
        },
        {
            "name": "biomedicalConceptIds",
            "baseName": "biomedicalConceptIds",
            "type": "Array<string | null>",
            "format": ""
        },
        {
            "name": "bcCategoryIds",
            "baseName": "bcCategoryIds",
            "type": "Array<string | null>",
            "format": ""
        },
        {
            "name": "bcSurrogateIds",
            "baseName": "bcSurrogateIds",
            "type": "Array<string | null>",
            "format": ""
        },
        {
            "name": "timelineId",
            "baseName": "timelineId",
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
            "type": "ActivityInputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ActivityInput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum ActivityInputInstanceTypeEnum {
    Activity = 'Activity'
}

