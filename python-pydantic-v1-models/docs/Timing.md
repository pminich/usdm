# Timing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**Code**](Code.md) |  | 
**value** | **str** |  | 
**value_label** | **str** |  | 
**relative_to_from** | [**Code**](Code.md) |  | 
**relative_from_scheduled_instance_id** | **str** |  | 
**relative_to_scheduled_instance_id** | **str** |  | [optional] 
**window_lower** | **str** |  | [optional] 
**window_upper** | **str** |  | [optional] 
**window_label** | **str** |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.timing import Timing

# TODO update the JSON string below
json = "{}"
# create an instance of Timing from a JSON string
timing_instance = Timing.from_json(json)
# print the JSON string representation of the object
print Timing.to_json()

# convert the object into a dict
timing_dict = timing_instance.to_dict()
# create an instance of Timing from a dict
timing_from_dict = Timing.from_dict(timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


