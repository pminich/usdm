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



export class NarrativeContentItem {
    'id': string;
    'name': string;
    'text': string;
    'instanceType': NarrativeContentItemInstanceTypeEnum;

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
            "type": "NarrativeContentItemInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return NarrativeContentItem.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum NarrativeContentItemInstanceTypeEnum {
    NarrativeContentItem = 'NarrativeContentItem'
}

