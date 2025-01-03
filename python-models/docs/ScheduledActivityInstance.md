# ScheduledActivityInstance


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
**activity_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**encounter_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.scheduled_activity_instance import ScheduledActivityInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledActivityInstance from a JSON string
scheduled_activity_instance_instance = ScheduledActivityInstance.from_json(json)
# print the JSON string representation of the object
print(ScheduledActivityInstance.to_json())

# convert the object into a dict
scheduled_activity_instance_dict = scheduled_activity_instance_instance.to_dict()
# create an instance of ScheduledActivityInstance from a dict
scheduled_activity_instance_from_dict = ScheduledActivityInstance.from_dict(scheduled_activity_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


