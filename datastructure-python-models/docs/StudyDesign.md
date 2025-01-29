# StudyDesign

NCI C-Code: C15320 Definition: A plan detailing how a study will be performed in order to represent the phenomenon under examination, to answer the research questions that have been asked, and informing the statistical approach. Preferred Term: Study Design

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**rationale** | **str** |  | 
**activities** | **List[str]** |  | [optional] 
**study_phase** | **str** |  | [optional] 
**biospecimen_retentions** | **List[str]** |  | [optional] 
**study_type** | **str** |  | [optional] 
**therapeutic_areas** | **List[str]** |  | [optional] 
**characteristics** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**encounters** | **List[str]** |  | [optional] 
**estimands** | **List[str]** |  | [optional] 
**indications** | **List[str]** |  | [optional] 
**objectives** | **List[str]** |  | [optional] 
**schedule_timelines** | **List[str]** |  | [optional] 
**arms** | **List[str]** |  | 
**study_cells** | **List[str]** |  | 
**document_versions** | **List[str]** |  | [optional] 
**elements** | **List[str]** |  | [optional] 
**study_interventions** | **List[str]** |  | [optional] 
**epochs** | **List[str]** |  | 
**population** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_design import StudyDesign

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDesign from a JSON string
study_design_instance = StudyDesign.from_json(json)
# print the JSON string representation of the object
print(StudyDesign.to_json())

# convert the object into a dict
study_design_dict = study_design_instance.to_dict()
# create an instance of StudyDesign from a dict
study_design_from_dict = StudyDesign.from_dict(study_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


