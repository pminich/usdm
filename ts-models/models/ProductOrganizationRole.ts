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


export class ProductOrganizationRole {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'code': Code;
    'appliesToIds'?: Array<string>;
    'organizationId': string;
    'instanceType': ProductOrganizationRoleInstanceTypeEnum;

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
            "name": "label",
            "baseName": "label",
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
            "name": "code",
            "baseName": "code",
            "type": "Code",
            "format": ""
        },
        {
            "name": "appliesToIds",
            "baseName": "appliesToIds",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "organizationId",
            "baseName": "organizationId",
            "type": "string",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "ProductOrganizationRoleInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ProductOrganizationRole.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum ProductOrganizationRoleInstanceTypeEnum {
    ProductOrganizationRole = 'ProductOrganizationRole'
}

