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
import { TransitionRule } from '../models/TransitionRule';


export class EncounterInput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'type': Code;
    'previousId'?: string | null;
    'nextId'?: string | null;
    'scheduledAtId'?: string | null;
    'environmentalSettings'?: Array<Code>;
    'contactModes'?: Array<Code>;
    'transitionStartRule'?: TransitionRule | null;
    'transitionEndRule'?: TransitionRule | null;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': EncounterInputInstanceTypeEnum;

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
            "name": "type",
            "baseName": "type",
            "type": "Code",
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
            "name": "scheduledAtId",
            "baseName": "scheduledAtId",
            "type": "string",
            "format": ""
        },
        {
            "name": "environmentalSettings",
            "baseName": "environmentalSettings",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "contactModes",
            "baseName": "contactModes",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "transitionStartRule",
            "baseName": "transitionStartRule",
            "type": "TransitionRule",
            "format": ""
        },
        {
            "name": "transitionEndRule",
            "baseName": "transitionEndRule",
            "type": "TransitionRule",
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
            "type": "EncounterInputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return EncounterInput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum EncounterInputInstanceTypeEnum {
    Encounter = 'Encounter'
}
