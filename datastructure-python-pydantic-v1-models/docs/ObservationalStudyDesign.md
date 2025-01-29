# ObservationalStudyDesign

NCI C-Code: CNEW Definition: The strategy that specifies the structure of an observational study in terms of the planned activities (including timing) and statistical analysis approach intended to meet the objectives of the study. Preferred Term: Observational Study Design

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
**time_perspective** | **str** |  | 
**sub_types** | **List[str]** |  | [optional] 
**model** | **str** |  | 
**sampling_method** | **str** |  | [optional] 
**biomedical_concepts** | **List[str]** |  | [optional] 
**bc_categories** | **List[str]** |  | [optional] 
**bc_surrogates** | **List[str]** |  | [optional] 
**analysis_populations** | **List[str]** |  | [optional] 
**dictionaries** | **List[str]** |  | [optional] 
**conditions** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.observational_study_design import ObservationalStudyDesign

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationalStudyDesign from a JSON string
observational_study_design_instance = ObservationalStudyDesign.from_json(json)
# print the JSON string representation of the object
print ObservationalStudyDesign.to_json()

# convert the object into a dict
observational_study_design_dict = observational_study_design_instance.to_dict()
# create an instance of ObservationalStudyDesign from a dict
observational_study_design_from_dict = ObservationalStudyDesign.from_dict(observational_study_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


