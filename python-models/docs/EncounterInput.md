# EncounterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**previous_id** | **str** |  | [optional] 
**next_id** | **str** |  | [optional] 
**scheduled_at_id** | **str** |  | [optional] 
**environmental_settings** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**contact_modes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**transition_start_rule** | [**TransitionRule**](TransitionRule.md) |  | [optional] 
**transition_end_rule** | [**TransitionRule**](TransitionRule.md) |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.encounter_input import EncounterInput

# TODO update the JSON string below
json = "{}"
# create an instance of EncounterInput from a JSON string
encounter_input_instance = EncounterInput.from_json(json)
# print the JSON string representation of the object
print(EncounterInput.to_json())

# convert the object into a dict
encounter_input_dict = encounter_input_instance.to_dict()
# create an instance of EncounterInput from a dict
encounter_input_from_dict = EncounterInput.from_dict(encounter_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


