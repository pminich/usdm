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
* NCI C-Code: C188810 Definition: A partitioning of a study arm into individual pieces, which are associated with an epoch and any number of sequential elements within that epoch. Preferred Term: Study Design Cell
*/
export class StudyCell {
    'id': string;
    'arm': string;
    'epoch': string;
    'elements'?: Array<string>;
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
            "name": "arm",
            "baseName": "arm",
            "type": "string",
            "format": ""
        },
        {
            "name": "epoch",
            "baseName": "epoch",
            "type": "string",
            "format": ""
        },
        {
            "name": "elements",
            "baseName": "elements",
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
        return StudyCell.attributeTypeMap;
    }

    public constructor() {
    }
}
