/**
 * USDM to OpenAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { HttpFile } from '../http/http';

/**
* NCI C-Code: CNEW Definition: A representation of a particular edition or snapshot of the study definition document as it exists at a particular point in time. Preferred Term: Study Definition Document Version
*/
export class StudyDefinitionDocumentVersion {
    'id': string;
    'version': string;
    'status': string;
    'notes'?: Array<string>;
    'dateValues'?: Array<string>;
    'contents'?: Array<string>;
    'children'?: Array<string>;
    'instanceType'?: string;

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
            "name": "version",
            "baseName": "version",
            "type": "string",
            "format": ""
        },
        {
            "name": "status",
            "baseName": "status",
            "type": "string",
            "format": ""
        },
        {
            "name": "notes",
            "baseName": "notes",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "dateValues",
            "baseName": "dateValues",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "contents",
            "baseName": "contents",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "children",
            "baseName": "children",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "string",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return StudyDefinitionDocumentVersion.attributeTypeMap;
    }

    public constructor() {
    }
}
