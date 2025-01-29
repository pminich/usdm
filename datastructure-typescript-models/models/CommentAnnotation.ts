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
* NCI C-Code: C44272 Definition: An explanatory or critical comment, or other in-context information (e.g., pattern, motif, link), that has been associated with data or other types of information. Preferred Term: Comment Annotation
*/
export class CommentAnnotation {
    'id': string;
    'text': string;
    'codes'?: Array<string>;
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
            "name": "text",
            "baseName": "text",
            "type": "string",
            "format": ""
        },
        {
            "name": "codes",
            "baseName": "codes",
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
        return CommentAnnotation.attributeTypeMap;
    }

    public constructor() {
    }
}
