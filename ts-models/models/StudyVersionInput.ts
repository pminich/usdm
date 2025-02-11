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

import { AbbreviationInput } from '../models/AbbreviationInput';
import { AdministrableProductInput } from '../models/AdministrableProductInput';
import { Code } from '../models/Code';
import { CommentAnnotation } from '../models/CommentAnnotation';
import { EligibilityCriterionInput } from '../models/EligibilityCriterionInput';
import { GovernanceDateInput } from '../models/GovernanceDateInput';
import { MedicalDeviceInput } from '../models/MedicalDeviceInput';
import { NarrativeContentItem } from '../models/NarrativeContentItem';
import { OrganizationInput } from '../models/OrganizationInput';
import { ProductOrganizationRole } from '../models/ProductOrganizationRole';
import { ReferenceIdentifier } from '../models/ReferenceIdentifier';
import { StudyAmendmentInput } from '../models/StudyAmendmentInput';
import { StudyIdentifier } from '../models/StudyIdentifier';
import { StudyRole } from '../models/StudyRole';
import { StudyTitle } from '../models/StudyTitle';
import { StudyVersionInputStudyDesignsInner } from '../models/StudyVersionInputStudyDesignsInner';


export class StudyVersionInput {
    'id': string;
    'versionIdentifier': string;
    'rationale': string;
    'documentVersionIds'?: Array<string>;
    'dateValues'?: Array<GovernanceDateInput>;
    'amendments'?: Array<StudyAmendmentInput>;
    'businessTherapeuticAreas'?: Array<Code>;
    'studyIdentifiers': Array<StudyIdentifier>;
    'referenceIdentifiers'?: Array<ReferenceIdentifier>;
    'studyDesigns'?: Array<StudyVersionInputStudyDesignsInner>;
    'titles': Array<StudyTitle>;
    'criteria': Array<EligibilityCriterionInput>;
    'narrativeContentItems'?: Array<NarrativeContentItem>;
    'abbreviations'?: Array<AbbreviationInput>;
    'roles'?: Array<StudyRole>;
    'organizations'?: Array<OrganizationInput>;
    'administrableProducts'?: Array<AdministrableProductInput>;
    'medicalDevices'?: Array<MedicalDeviceInput>;
    'productOrganizationRoles'?: Array<ProductOrganizationRole>;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': StudyVersionInputInstanceTypeEnum;

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
            "type": "Array<GovernanceDateInput>",
            "format": ""
        },
        {
            "name": "amendments",
            "baseName": "amendments",
            "type": "Array<StudyAmendmentInput>",
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
            "type": "Array<StudyVersionInputStudyDesignsInner>",
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
            "type": "Array<EligibilityCriterionInput>",
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
            "type": "Array<AbbreviationInput>",
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
            "type": "Array<OrganizationInput>",
            "format": ""
        },
        {
            "name": "administrableProducts",
            "baseName": "administrableProducts",
            "type": "Array<AdministrableProductInput>",
            "format": ""
        },
        {
            "name": "medicalDevices",
            "baseName": "medicalDevices",
            "type": "Array<MedicalDeviceInput>",
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
            "type": "StudyVersionInputInstanceTypeEnum",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return StudyVersionInput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum StudyVersionInputInstanceTypeEnum {
    StudyVersion = 'StudyVersion'
}

