# ScheduleTimelineInputInstancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**default_condition_id** | **str** |  | [optional] 
**epoch_id** | **str** |  | [optional] 
**instance_type** | **str** |  | 
**timeline_id** | **str** |  | [optional] 
**timeline_exit_id** | **str** |  | [optional] 
**activity_ids** | **List[str]** |  | [optional] [default to []]
**encounter_id** | **str** |  | [optional] 
**condition_assignments** | [**List[ConditionAssignment]**](ConditionAssignment.md) |  | 

## Example

```python
from openapi_client.models.schedule_timeline_input_instances_inner import ScheduleTimelineInputInstancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTimelineInputInstancesInner from a JSON string
schedule_timeline_input_instances_inner_instance = ScheduleTimelineInputInstancesInner.from_json(json)
# print the JSON string representation of the object
print(ScheduleTimelineInputInstancesInner.to_json())

# convert the object into a dict
schedule_timeline_input_instances_inner_dict = schedule_timeline_input_instances_inner_instance.to_dict()
# create an instance of ScheduleTimelineInputInstancesInner from a dict
schedule_timeline_input_instances_inner_from_dict = ScheduleTimelineInputInstancesInner.from_dict(schedule_timeline_input_instances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


