# ScheduledActivityInstance

NCI C-Code: C201350 Definition: A scheduled occurrence of an activity event. Preferred Term: Scheduled Activity Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**default_condition** | **str** |  | [optional] 
**epoch** | **str** |  | [optional] 
**activities** | **List[str]** |  | [optional] 
**encounter** | **str** |  | [optional] 
**timeline** | **str** |  | [optional] 
**timeline_exit** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

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


