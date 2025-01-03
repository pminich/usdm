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

import { StudyInput } from '../models/StudyInput';


export class WrapperInput {
    'study': StudyInput;
    'usdmVersion': string;
    'systemName'?: string | null;
    'systemVersion'?: string | null;

    static readonly discriminator: string | undefined = undefined;

    static readonly mapping: {[index: string]: string} | undefined = undefined;

    static readonly attributeTypeMap: Array<{name: string, baseName: string, type: string, format: string}> = [
        {
            "name": "study",
            "baseName": "study",
            "type": "StudyInput",
            "format": ""
        },
        {
            "name": "usdmVersion",
            "baseName": "usdmVersion",
            "type": "string",
            "format": ""
        },
        {
            "name": "systemName",
            "baseName": "systemName",
            "type": "string",
            "format": ""
        },
        {
            "name": "systemVersion",
            "baseName": "systemVersion",
            "type": "string",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return WrapperInput.attributeTypeMap;
    }

    public constructor() {
    }
}