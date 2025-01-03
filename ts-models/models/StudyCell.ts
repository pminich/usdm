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



export class StudyCell {
    'id': string;
    'armId': string;
    'epochId': string;
    'elementIds'?: Array<string | null>;
    'instanceType': StudyCellInstanceTypeEnum;

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
            "name": "armId",
            "baseName": "armId",
            "type": "string",
            "format": ""
        },
        {
            "name": "epochId",
            "baseName": "epochId",
            "type": "string",
            "format": ""
        },
        {
            "name": "elementIds",
            "baseName": "elementIds",
            "type": "Array<string | null>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "StudyCellInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return StudyCell.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum StudyCellInstanceTypeEnum {
    StudyCell = 'StudyCell'
}
