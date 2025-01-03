# ScheduleTimelineOutput


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
from openapi_client.models.schedule_timeline_output import ScheduleTimelineOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTimelineOutput from a JSON string
schedule_timeline_output_instance = ScheduleTimelineOutput.from_json(json)
# print the JSON string representation of the object
print(ScheduleTimelineOutput.to_json())

# convert the object into a dict
schedule_timeline_output_dict = schedule_timeline_output_instance.to_dict()
# create an instance of ScheduleTimelineOutput from a dict
schedule_timeline_output_from_dict = ScheduleTimelineOutput.from_dict(schedule_timeline_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


