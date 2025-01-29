# Timing

NCI C-Code: C80484 Definition: The chronological relationship between temporal events. Preferred Term: Timing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**value** | **str** |  | 
**value_label** | **str** |  | 
**window_label** | **str** |  | 
**window_lower** | **str** |  | 
**window_upper** | **str** |  | 
**relative_to_from** | **str** |  | 
**type** | **str** |  | 
**relative_to_scheduled_instance** | **str** |  | [optional] 
**relative_from_scheduled_instance** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.timing import Timing

# TODO update the JSON string below
json = "{}"
# create an instance of Timing from a JSON string
timing_instance = Timing.from_json(json)
# print the JSON string representation of the object
print(Timing.to_json())

# convert the object into a dict
timing_dict = timing_instance.to_dict()
# create an instance of Timing from a dict
timing_from_dict = Timing.from_dict(timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


