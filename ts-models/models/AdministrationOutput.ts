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

import { AdministrationDurationOutput } from '../models/AdministrationDurationOutput';
import { AliasCode } from '../models/AliasCode';
import { CommentAnnotation } from '../models/CommentAnnotation';
import { QuantityOutput } from '../models/QuantityOutput';


export class AdministrationOutput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'duration': AdministrationDurationOutput;
    'dose': QuantityOutput | null;
    'route': AliasCode | null;
    'frequency': AliasCode | null;
    'administrableProductId'?: string | null;
    'medicalDeviceId'?: string | null;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': AdministrationOutputInstanceTypeEnum;

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
            "name": "duration",
            "baseName": "duration",
            "type": "AdministrationDurationOutput",
            "format": ""
        },
        {
            "name": "dose",
            "baseName": "dose",
            "type": "QuantityOutput",
            "format": ""
        },
        {
            "name": "route",
            "baseName": "route",
            "type": "AliasCode",
            "format": ""
        },
        {
            "name": "frequency",
            "baseName": "frequency",
            "type": "AliasCode",
            "format": ""
        },
        {
            "name": "administrableProductId",
            "baseName": "administrableProductId",
            "type": "string",
            "format": ""
        },
        {
            "name": "medicalDeviceId",
            "baseName": "medicalDeviceId",
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
            "type": "AdministrationOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return AdministrationOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum AdministrationOutputInstanceTypeEnum {
    Administration = 'Administration'
}

