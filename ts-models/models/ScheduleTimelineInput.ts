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

import { ScheduleTimelineExit } from '../models/ScheduleTimelineExit';
import { ScheduleTimelineInputInstancesInner } from '../models/ScheduleTimelineInputInstancesInner';
import { Timing } from '../models/Timing';


export class ScheduleTimelineInput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'mainTimeline': boolean;
    'entryCondition': string;
    'entryId': string;
    'exits'?: Array<ScheduleTimelineExit>;
    'timings'?: Array<Timing>;
    'instances'?: Array<ScheduleTimelineInputInstancesInner>;
    'instanceType': ScheduleTimelineInputInstanceTypeEnum;

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
            "name": "mainTimeline",
            "baseName": "mainTimeline",
            "type": "boolean",
            "format": ""
        },
        {
            "name": "entryCondition",
            "baseName": "entryCondition",
            "type": "string",
            "format": ""
        },
        {
            "name": "entryId",
            "baseName": "entryId",
            "type": "string",
            "format": ""
        },
        {
            "name": "exits",
            "baseName": "exits",
            "type": "Array<ScheduleTimelineExit>",
            "format": ""
        },
        {
            "name": "timings",
            "baseName": "timings",
            "type": "Array<Timing>",
            "format": ""
        },
        {
            "name": "instances",
            "baseName": "instances",
            "type": "Array<ScheduleTimelineInputInstancesInner>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "ScheduleTimelineInputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ScheduleTimelineInput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum ScheduleTimelineInputInstanceTypeEnum {
    ScheduleTimeline = 'ScheduleTimeline'
}
