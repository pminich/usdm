# EncounterOutput


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
from openapi_client.models.encounter_output import EncounterOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EncounterOutput from a JSON string
encounter_output_instance = EncounterOutput.from_json(json)
# print the JSON string representation of the object
print(EncounterOutput.to_json())

# convert the object into a dict
encounter_output_dict = encounter_output_instance.to_dict()
# create an instance of EncounterOutput from a dict
encounter_output_from_dict = EncounterOutput.from_dict(encounter_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


