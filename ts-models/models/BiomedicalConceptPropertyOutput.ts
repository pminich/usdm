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
import { CommentAnnotation } from '../models/CommentAnnotation';
import { ResponseCode } from '../models/ResponseCode';


export class BiomedicalConceptPropertyOutput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'isRequired': boolean;
    'isEnabled': boolean;
    'datatype': string;
    'responseCodes'?: Array<ResponseCode>;
    'code': AliasCode | null;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': BiomedicalConceptPropertyOutputInstanceTypeEnum;

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
            "name": "isRequired",
            "baseName": "isRequired",
            "type": "boolean",
            "format": ""
        },
        {
            "name": "isEnabled",
            "baseName": "isEnabled",
            "type": "boolean",
            "format": ""
        },
        {
            "name": "datatype",
            "baseName": "datatype",
            "type": "string",
            "format": ""
        },
        {
            "name": "responseCodes",
            "baseName": "responseCodes",
            "type": "Array<ResponseCode>",
            "format": ""
        },
        {
            "name": "code",
            "baseName": "code",
            "type": "AliasCode",
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
            "type": "BiomedicalConceptPropertyOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return BiomedicalConceptPropertyOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum BiomedicalConceptPropertyOutputInstanceTypeEnum {
    BiomedicalConceptProperty = 'BiomedicalConceptProperty'
}
