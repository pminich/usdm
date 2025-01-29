# Encounter

NCI C-Code: CNEW Definition: Any physical or virtual contact between two or more parties involved in a study, at which an assessment or activity takes place. Preferred Term: Study Encounter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**environmental_settings** | **List[str]** |  | [optional] 
**contact_modes** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**transition_end_rule** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**transition_start_rule** | **str** |  | [optional] 
**scheduled_at** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.encounter import Encounter

# TODO update the JSON string below
json = "{}"
# create an instance of Encounter from a JSON string
encounter_instance = Encounter.from_json(json)
# print the JSON string representation of the object
print Encounter.to_json()

# convert the object into a dict
encounter_dict = encounter_instance.to_dict()
# create an instance of Encounter from a dict
encounter_from_dict = Encounter.from_dict(encounter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


