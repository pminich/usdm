# InterventionalStudyDesign

NCI C-Code: CNEW Definition: The strategy that specifies the structure of an interventional trial in terms of the planned activities (including timing) and statistical analysis approach intended to meet the objectives of the study. Preferred Term: Interventional Study Design

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
**sub_types** | **List[str]** |  | [optional] 
**intent_types** | **List[str]** |  | [optional] 
**model** | **str** |  | 
**blinding_schema** | **str** |  | [optional] 
**biomedical_concepts** | **List[str]** |  | [optional] 
**bc_categories** | **List[str]** |  | [optional] 
**bc_surrogates** | **List[str]** |  | [optional] 
**analysis_populations** | **List[str]** |  | [optional] 
**dictionaries** | **List[str]** |  | [optional] 
**conditions** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.interventional_study_design import InterventionalStudyDesign

# TODO update the JSON string below
json = "{}"
# create an instance of InterventionalStudyDesign from a JSON string
interventional_study_design_instance = InterventionalStudyDesign.from_json(json)
# print the JSON string representation of the object
print InterventionalStudyDesign.to_json()

# convert the object into a dict
interventional_study_design_dict = interventional_study_design_instance.to_dict()
# create an instance of InterventionalStudyDesign from a dict
interventional_study_design_from_dict = InterventionalStudyDesign.from_dict(interventional_study_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


