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


export class CommentAnnotation {
    'id': string;
    'text': string;
    'codes'?: Array<Code>;
    'instanceType': CommentAnnotationInstanceTypeEnum;

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
            "name": "text",
            "baseName": "text",
            "type": "string",
            "format": ""
        },
        {
            "name": "codes",
            "baseName": "codes",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "CommentAnnotationInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return CommentAnnotation.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum CommentAnnotationInstanceTypeEnum {
    CommentAnnotation = 'CommentAnnotation'
}
