# ScheduleTimeline

NCI C-Code: C201348 Definition: A chronological schedule of planned temporal events. Preferred Term: Schedule Timeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**entry_condition** | **str** |  | 
**main_timeline** | **str** |  | 
**instances** | **List[str]** |  | [optional] 
**entry** | **str** |  | 
**exits** | **List[str]** |  | [optional] 
**timings** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_timeline import ScheduleTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTimeline from a JSON string
schedule_timeline_instance = ScheduleTimeline.from_json(json)
# print the JSON string representation of the object
print ScheduleTimeline.to_json()

# convert the object into a dict
schedule_timeline_dict = schedule_timeline_instance.to_dict()
# create an instance of ScheduleTimeline from a dict
schedule_timeline_from_dict = ScheduleTimeline.from_dict(schedule_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


