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
* NCI C-Code: CNEW Definition: An individual item within the container that holds an instance of unstructured text and which may include objects such as tables, figures, and images. Preferred Term: Narrative Content Item
*/
export class NarrativeContentItem {
    'id': string;
    'name': string;
    'text': string;
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
            "name": "name",
            "baseName": "name",
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
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "string",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return NarrativeContentItem.attributeTypeMap;
    }

    public constructor() {
    }
}
