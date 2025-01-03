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

import { ActivityOutput } from '../models/ActivityOutput';
import { AliasCode } from '../models/AliasCode';
import { AnalysisPopulationOutput } from '../models/AnalysisPopulationOutput';
import { BiomedicalConceptCategoryOutput } from '../models/BiomedicalConceptCategoryOutput';
import { BiomedicalConceptOutput } from '../models/BiomedicalConceptOutput';
import { BiomedicalConceptSurrogateOutput } from '../models/BiomedicalConceptSurrogateOutput';
import { BiospecimenRetention } from '../models/BiospecimenRetention';
import { Code } from '../models/Code';
import { CommentAnnotation } from '../models/CommentAnnotation';
import { ConditionOutput } from '../models/ConditionOutput';
import { EncounterOutput } from '../models/EncounterOutput';
import { EstimandOutput } from '../models/EstimandOutput';
import { IndicationOutput } from '../models/IndicationOutput';
import { ObjectiveOutput } from '../models/ObjectiveOutput';
import { ScheduleTimelineOutput } from '../models/ScheduleTimelineOutput';
import { StudyArmOutput } from '../models/StudyArmOutput';
import { StudyCell } from '../models/StudyCell';
import { StudyDesignPopulationOutput } from '../models/StudyDesignPopulationOutput';
import { StudyElementOutput } from '../models/StudyElementOutput';
import { StudyEpochOutput } from '../models/StudyEpochOutput';
import { StudyInterventionOutput } from '../models/StudyInterventionOutput';
import { SyntaxTemplateDictionary } from '../models/SyntaxTemplateDictionary';


export class ObservationalStudyDesignOutput {
    'id': string;
    'name': string;
    'label'?: string | null;
    'description'?: string | null;
    'studyType'?: Code | null;
    'studyPhase'?: AliasCode | null;
    'therapeuticAreas'?: Array<Code>;
    'characteristics'?: Array<Code>;
    'encounters'?: Array<EncounterOutput>;
    'activities'?: Array<ActivityOutput>;
    'biomedicalConcepts'?: Array<BiomedicalConceptOutput>;
    'bcCategories'?: Array<BiomedicalConceptCategoryOutput>;
    'bcSurrogates'?: Array<BiomedicalConceptSurrogateOutput>;
    'arms': Array<StudyArmOutput>;
    'studyCells': Array<StudyCell>;
    'rationale': string;
    'epochs': Array<StudyEpochOutput>;
    'elements'?: Array<StudyElementOutput>;
    'estimands'?: Array<EstimandOutput>;
    'indications'?: Array<IndicationOutput>;
    'studyInterventions'?: Array<StudyInterventionOutput>;
    'objectives'?: Array<ObjectiveOutput>;
    'population'?: StudyDesignPopulationOutput | null;
    'analysisPopulations'?: Array<AnalysisPopulationOutput>;
    'scheduleTimelines'?: Array<ScheduleTimelineOutput>;
    'biospecimenRetentions'?: Array<BiospecimenRetention>;
    'documentVersionIds'?: Array<string>;
    'dictionaries'?: Array<SyntaxTemplateDictionary>;
    'conditions'?: Array<ConditionOutput>;
    'notes'?: Array<CommentAnnotation>;
    'instanceType': ObservationalStudyDesignOutputInstanceTypeEnum;
    'subTypes'?: Array<Code>;
    'model': Code;
    'timePerspective': Code;
    'samplingMethod'?: Code | null;

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
            "name": "studyType",
            "baseName": "studyType",
            "type": "Code",
            "format": ""
        },
        {
            "name": "studyPhase",
            "baseName": "studyPhase",
            "type": "AliasCode",
            "format": ""
        },
        {
            "name": "therapeuticAreas",
            "baseName": "therapeuticAreas",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "characteristics",
            "baseName": "characteristics",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "encounters",
            "baseName": "encounters",
            "type": "Array<EncounterOutput>",
            "format": ""
        },
        {
            "name": "activities",
            "baseName": "activities",
            "type": "Array<ActivityOutput>",
            "format": ""
        },
        {
            "name": "biomedicalConcepts",
            "baseName": "biomedicalConcepts",
            "type": "Array<BiomedicalConceptOutput>",
            "format": ""
        },
        {
            "name": "bcCategories",
            "baseName": "bcCategories",
            "type": "Array<BiomedicalConceptCategoryOutput>",
            "format": ""
        },
        {
            "name": "bcSurrogates",
            "baseName": "bcSurrogates",
            "type": "Array<BiomedicalConceptSurrogateOutput>",
            "format": ""
        },
        {
            "name": "arms",
            "baseName": "arms",
            "type": "Array<StudyArmOutput>",
            "format": ""
        },
        {
            "name": "studyCells",
            "baseName": "studyCells",
            "type": "Array<StudyCell>",
            "format": ""
        },
        {
            "name": "rationale",
            "baseName": "rationale",
            "type": "string",
            "format": ""
        },
        {
            "name": "epochs",
            "baseName": "epochs",
            "type": "Array<StudyEpochOutput>",
            "format": ""
        },
        {
            "name": "elements",
            "baseName": "elements",
            "type": "Array<StudyElementOutput>",
            "format": ""
        },
        {
            "name": "estimands",
            "baseName": "estimands",
            "type": "Array<EstimandOutput>",
            "format": ""
        },
        {
            "name": "indications",
            "baseName": "indications",
            "type": "Array<IndicationOutput>",
            "format": ""
        },
        {
            "name": "studyInterventions",
            "baseName": "studyInterventions",
            "type": "Array<StudyInterventionOutput>",
            "format": ""
        },
        {
            "name": "objectives",
            "baseName": "objectives",
            "type": "Array<ObjectiveOutput>",
            "format": ""
        },
        {
            "name": "population",
            "baseName": "population",
            "type": "StudyDesignPopulationOutput",
            "format": ""
        },
        {
            "name": "analysisPopulations",
            "baseName": "analysisPopulations",
            "type": "Array<AnalysisPopulationOutput>",
            "format": ""
        },
        {
            "name": "scheduleTimelines",
            "baseName": "scheduleTimelines",
            "type": "Array<ScheduleTimelineOutput>",
            "format": ""
        },
        {
            "name": "biospecimenRetentions",
            "baseName": "biospecimenRetentions",
            "type": "Array<BiospecimenRetention>",
            "format": ""
        },
        {
            "name": "documentVersionIds",
            "baseName": "documentVersionIds",
            "type": "Array<string>",
            "format": ""
        },
        {
            "name": "dictionaries",
            "baseName": "dictionaries",
            "type": "Array<SyntaxTemplateDictionary>",
            "format": ""
        },
        {
            "name": "conditions",
            "baseName": "conditions",
            "type": "Array<ConditionOutput>",
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
            "type": "ObservationalStudyDesignOutputInstanceTypeEnum",
            "format": ""
        },
        {
            "name": "subTypes",
            "baseName": "subTypes",
            "type": "Array<Code>",
            "format": ""
        },
        {
            "name": "model",
            "baseName": "model",
            "type": "Code",
            "format": ""
        },
        {
            "name": "timePerspective",
            "baseName": "timePerspective",
            "type": "Code",
            "format": ""
        },
        {
            "name": "samplingMethod",
            "baseName": "samplingMethod",
            "type": "Code",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ObservationalStudyDesignOutput.attributeTypeMap;
    }

    public constructor() {
    }
}

export enum ObservationalStudyDesignOutputInstanceTypeEnum {
    ObservationalStudyDesign = 'ObservationalStudyDesign'
}

