# StudyVersionInputStudyDesignsInner


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
**encounters** | [**List[EncounterInput]**](EncounterInput.md) |  | [optional] [default to []]
**activities** | [**List[ActivityInput]**](ActivityInput.md) |  | [optional] [default to []]
**biomedical_concepts** | [**List[BiomedicalConceptInput]**](BiomedicalConceptInput.md) |  | [optional] [default to []]
**bc_categories** | [**List[BiomedicalConceptCategoryInput]**](BiomedicalConceptCategoryInput.md) |  | [optional] [default to []]
**bc_surrogates** | [**List[BiomedicalConceptSurrogateInput]**](BiomedicalConceptSurrogateInput.md) |  | [optional] [default to []]
**arms** | [**List[StudyArmInput]**](StudyArmInput.md) |  | 
**study_cells** | [**List[StudyCell]**](StudyCell.md) |  | 
**rationale** | **str** |  | 
**epochs** | [**List[StudyEpochInput]**](StudyEpochInput.md) |  | 
**elements** | [**List[StudyElementInput]**](StudyElementInput.md) |  | [optional] [default to []]
**estimands** | [**List[EstimandInput]**](EstimandInput.md) |  | [optional] [default to []]
**indications** | [**List[IndicationInput]**](IndicationInput.md) |  | [optional] [default to []]
**study_interventions** | [**List[StudyInterventionInput]**](StudyInterventionInput.md) |  | [optional] [default to []]
**objectives** | [**List[ObjectiveInput]**](ObjectiveInput.md) |  | [optional] [default to []]
**population** | [**StudyDesignPopulationInput**](StudyDesignPopulationInput.md) |  | [optional] 
**analysis_populations** | [**List[AnalysisPopulationInput]**](AnalysisPopulationInput.md) |  | [optional] [default to []]
**schedule_timelines** | [**List[ScheduleTimelineInput]**](ScheduleTimelineInput.md) |  | [optional] [default to []]
**biospecimen_retentions** | [**List[BiospecimenRetention]**](BiospecimenRetention.md) |  | [optional] [default to []]
**document_version_ids** | **List[str]** |  | [optional] [default to []]
**dictionaries** | [**List[SyntaxTemplateDictionary]**](SyntaxTemplateDictionary.md) |  | [optional] [default to []]
**conditions** | [**List[ConditionInput]**](ConditionInput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 
**sub_types** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**model** | [**Code**](Code.md) |  | 
**intent_types** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**blinding_schema** | [**AliasCode**](AliasCode.md) |  | [optional] 
**time_perspective** | [**Code**](Code.md) |  | 
**sampling_method** | [**Code**](Code.md) |  | [optional] 

## Example

```python
from openapi_client.models.study_version_input_study_designs_inner import StudyVersionInputStudyDesignsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudyVersionInputStudyDesignsInner from a JSON string
study_version_input_study_designs_inner_instance = StudyVersionInputStudyDesignsInner.from_json(json)
# print the JSON string representation of the object
print(StudyVersionInputStudyDesignsInner.to_json())

# convert the object into a dict
study_version_input_study_designs_inner_dict = study_version_input_study_designs_inner_instance.to_dict()
# create an instance of StudyVersionInputStudyDesignsInner from a dict
study_version_input_study_designs_inner_from_dict = StudyVersionInputStudyDesignsInner.from_dict(study_version_input_study_designs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


