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
* NCI C-Code: C45306 Definition: Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical. Preferred Term: Substance
*/
export class Substance {
    'id': string;
    'name': string;
    'description': string;
    'label': string;
    'codes'?: Array<string>;
    'strengths': Array<string>;
    'referenceSubstance'?: string;
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
            "name": "codes",
            "baseName": "codes",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "strengths",
            "baseName": "strengths",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "referenceSubstance",
            "baseName": "referenceSubstance",
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
        return Substance.attributeTypeMap;
    }

    public constructor() {
    }
}
