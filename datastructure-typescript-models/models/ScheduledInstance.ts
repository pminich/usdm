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
* NCI C-Code: C201299 Definition: A scheduled occurrence of a temporal event. Preferred Term: Scheduled Instance
*/
export class ScheduledInstance {
    'id': string;
    'name': string;
    'description': string;
    'label': string;
    'defaultCondition'?: string;
    'epoch'?: string;

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
            "name": "description",
            "baseName": "description",
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
            "name": "defaultCondition",
            "baseName": "defaultCondition",
            "type": "string",
            "format": ""
        },
        {
            "name": "epoch",
            "baseName": "epoch",
            "type": "string",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ScheduledInstance.attributeTypeMap;
    }

    public constructor() {
    }
}
