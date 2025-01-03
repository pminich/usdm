# ScheduleTimelineInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**main_timeline** | **bool** |  | 
**entry_condition** | **str** |  | 
**entry_id** | **str** |  | 
**exits** | [**List[ScheduleTimelineExit]**](ScheduleTimelineExit.md) |  | [optional] [default to []]
**timings** | [**List[Timing]**](Timing.md) |  | [optional] [default to []]
**instances** | [**List[ScheduleTimelineInputInstancesInner]**](ScheduleTimelineInputInstancesInner.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.schedule_timeline_input import ScheduleTimelineInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTimelineInput from a JSON string
schedule_timeline_input_instance = ScheduleTimelineInput.from_json(json)
# print the JSON string representation of the object
print ScheduleTimelineInput.to_json()

# convert the object into a dict
schedule_timeline_input_dict = schedule_timeline_input_instance.to_dict()
# create an instance of ScheduleTimelineInput from a dict
schedule_timeline_input_from_dict = ScheduleTimelineInput.from_dict(schedule_timeline_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


