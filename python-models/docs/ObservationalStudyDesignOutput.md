# ObservationalStudyDesignOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**study_type** | [**Code**](Code.md) |  | [optional] 
**study_phase** | [**AliasCode**](AliasCode.md) |  | [optional] 
**therapeutic_areas** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**characteristics** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**encounters** | [**List[EncounterOutput]**](EncounterOutput.md) |  | [optional] [default to []]
**activities** | [**List[ActivityOutput]**](ActivityOutput.md) |  | [optional] [default to []]
**biomedical_concepts** | [**List[BiomedicalConceptOutput]**](BiomedicalConceptOutput.md) |  | [optional] [default to []]
**bc_categories** | [**List[BiomedicalConceptCategoryOutput]**](BiomedicalConceptCategoryOutput.md) |  | [optional] [default to []]
**bc_surrogates** | [**List[BiomedicalConceptSurrogateOutput]**](BiomedicalConceptSurrogateOutput.md) |  | [optional] [default to []]
**arms** | [**List[StudyArmOutput]**](StudyArmOutput.md) |  | 
**study_cells** | [**List[StudyCell]**](StudyCell.md) |  | 
**rationale** | **str** |  | 
**epochs** | [**List[StudyEpochOutput]**](StudyEpochOutput.md) |  | 
**elements** | [**List[StudyElementOutput]**](StudyElementOutput.md) |  | [optional] [default to []]
**estimands** | [**List[EstimandOutput]**](EstimandOutput.md) |  | [optional] [default to []]
**indications** | [**List[IndicationOutput]**](IndicationOutput.md) |  | [optional] [default to []]
**study_interventions** | [**List[StudyInterventionOutput]**](StudyInterventionOutput.md) |  | [optional] [default to []]
**objectives** | [**List[ObjectiveOutput]**](ObjectiveOutput.md) |  | [optional] [default to []]
**population** | [**StudyDesignPopulationOutput**](StudyDesignPopulationOutput.md) |  | [optional] 
**analysis_populations** | [**List[AnalysisPopulationOutput]**](AnalysisPopulationOutput.md) |  | [optional] [default to []]
**schedule_timelines** | [**List[ScheduleTimelineOutput]**](ScheduleTimelineOutput.md) |  | [optional] [default to []]
**biospecimen_retentions** | [**List[BiospecimenRetention]**](BiospecimenRetention.md) |  | [optional] [default to []]
**document_version_ids** | **List[str]** |  | [optional] [default to []]
**dictionaries** | [**List[SyntaxTemplateDictionary]**](SyntaxTemplateDictionary.md) |  | [optional] [default to []]
**conditions** | [**List[ConditionOutput]**](ConditionOutput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 
**sub_types** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**model** | [**Code**](Code.md) |  | 
**time_perspective** | [**Code**](Code.md) |  | 
**sampling_method** | [**Code**](Code.md) |  | [optional] 

## Example

```python
from openapi_client.models.observational_study_design_output import ObservationalStudyDesignOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationalStudyDesignOutput from a JSON string
observational_study_design_output_instance = ObservationalStudyDesignOutput.from_json(json)
# print the JSON string representation of the object
print(ObservationalStudyDesignOutput.to_json())

# convert the object into a dict
observational_study_design_output_dict = observational_study_design_output_instance.to_dict()
# create an instance of ObservationalStudyDesignOutput from a dict
observational_study_design_output_from_dict = ObservationalStudyDesignOutput.from_dict(observational_study_design_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


