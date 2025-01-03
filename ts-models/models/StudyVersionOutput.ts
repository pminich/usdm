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

import { AbbreviationOutput } from '../models/AbbreviationOutput';
import { AdministrableProductOutput } from '../models/AdministrableProductOutput';
import { Code } from '../models/Code';
import { CommentAnnotation } from '../models/CommentAnnotation';
import { EligibilityCriterionOutput } from '../models/EligibilityCriterionOutput';
import { GovernanceDateOutput } from '../models/GovernanceDateOutput';
import { MedicalDeviceOutput } from '../models/MedicalDeviceOutput';
import { NarrativeContentItem } from '../models/NarrativeContentItem';
import { OrganizationOutput } from '../models/OrganizationOutput';
import { ProductOrganizationRole } from '../models/ProductOrganizationRole';
import { ReferenceIdentifier } from '../models/ReferenceIdentifier';
import { SearchStudyDesignV3StudyDesignsGet200ResponseInner } from '../models/SearchStudyDesignV3StudyDesignsGet200ResponseInner';
import { StudyAmendmentOutput } from '../models/StudyAmendmentOutput';
import { StudyIdentifier } from '../models/StudyIdentifier';
import { StudyRole } from '../models/StudyRole';
import { StudyTitle } from '../models/StudyTitle';


export class StudyVersionOutput {
    'id': string;
    'versionIdentifier': string;
    'rationale': string;
    'documentVersionIds'?: Array<string>;
    'dateValues'?: Array<GovernanceDateOutput>;
    'amendments'?: Array<StudyAmendmentOutput>;
    'businessTherapeuticAreas'?: Array<Code>;
    'studyIdentifiers': Array<StudyIdentifier>;
    'referenceIdentifiers'?: Array<ReferenceIdentifier>;
    'studyDesigns'?: Array<SearchStudyDesignV3StudyDesignsGet200ResponseInner>;
    'titles': Array<StudyTitle>;
    'criteria': Array<EligibilityCriterionOutput>;
    'narrativeContentItems'?: Array<NarrativeContentItem>;
    'abbreviations'?: Array<AbbreviationOutput>;
    'roles'?: Array<StudyRole>;
    'organizations'?: Array<OrganizationOutput>;
    'administrableProducts'?: Array<AdministrableProductOutput>;
    'medicalDevices'?: Array<MedicalDeviceOutput>;
    'productOrganizationRoles'?: Array<ProductOrganizationRole>;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': StudyVersionOutputInstanceTypeEnum;

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
            "name": "versionIdentifier",
            "baseName": "versionIdentifier",
            "type": "string",
            "format": ""
        },
        {
            "name": "rationale",
            "baseName": "rationale",
            "type": "string",
            "format": ""
        },
        {
            "name": "documentVersionIds",
            "baseName": "documentVersionIds",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "dateValues",
            "baseName": "dateValues",
            "type": "Array<GovernanceDateOutput>",
            "format": ""
        },
        {
            "name": "amendments",
            "baseName": "amendments",
            "type": "Array<StudyAmendmentOutput>",
            "format": ""
        },
        {
            "name": "businessTherapeuticAreas",
            "baseName": "businessTherapeuticAreas",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "studyIdentifiers",
            "baseName": "studyIdentifiers",
            "type": "Array<StudyIdentifier>",
            "format": ""
        },
        {
            "name": "referenceIdentifiers",
            "baseName": "referenceIdentifiers",
            "type": "Array<ReferenceIdentifier>",
            "format": ""
        },
        {
            "name": "studyDesigns",
            "baseName": "studyDesigns",
            "type": "Array<SearchStudyDesignV3StudyDesignsGet200ResponseInner>",
            "format": ""
        },
        {
            "name": "titles",
            "baseName": "titles",
            "type": "Array<StudyTitle>",
            "format": ""
        },
        {
            "name": "criteria",
            "baseName": "criteria",
            "type": "Array<EligibilityCriterionOutput>",
            "format": ""
        },
        {
            "name": "narrativeContentItems",
            "baseName": "narrativeContentItems",
            "type": "Array<NarrativeContentItem>",
            "format": ""
        },
        {
            "name": "abbreviations",
            "baseName": "abbreviations",
            "type": "Array<AbbreviationOutput>",
            "format": ""
        },
        {
            "name": "roles",
            "baseName": "roles",
            "type": "Array<StudyRole>",
            "format": ""
        },
        {
            "name": "organizations",
            "baseName": "organizations",
            "type": "Array<OrganizationOutput>",
            "format": ""
        },
        {
            "name": "administrableProducts",
            "baseName": "administrableProducts",
            "type": "Array<AdministrableProductOutput>",
            "format": ""
        },
        {
            "name": "medicalDevices",
            "baseName": "medicalDevices",
            "type": "Array<MedicalDeviceOutput>",
            "format": ""
        },
        {
            "name": "productOrganizationRoles",
            "baseName": "productOrganizationRoles",
            "type": "Array<ProductOrganizationRole>",
            "format": ""
        },
        {
            "name": "notes",
            "baseName": "notes",
            "type": "Array<CommentAnnotation>",
            "format": ""
        },
        {
            "name": "instanceType",
            "baseName": "instanceType",
            "type": "StudyVersionOutputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return StudyVersionOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum StudyVersionOutputInstanceTypeEnum {
    StudyVersion = 'StudyVersion'
}

