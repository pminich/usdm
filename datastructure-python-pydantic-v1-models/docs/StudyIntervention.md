# StudyIntervention

NCI C-Code: C207649 Definition: Any agent, device, or procedure being tested or used as a reference or comparator in the conduct of a clinical trial. Preferred Term: Study Intervention

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**administrations** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**role** | **str** |  | 
**codes** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**minimum_response_duration** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_intervention import StudyIntervention

# TODO update the JSON string below
json = "{}"
# create an instance of StudyIntervention from a JSON string
study_intervention_instance = StudyIntervention.from_json(json)
# print the JSON string representation of the object
print StudyIntervention.to_json()

# convert the object into a dict
study_intervention_dict = study_intervention_instance.to_dict()
# create an instance of StudyIntervention from a dict
study_intervention_from_dict = StudyIntervention.from_dict(study_intervention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


