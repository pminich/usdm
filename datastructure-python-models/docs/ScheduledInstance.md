# ScheduledInstance

NCI C-Code: C201299 Definition: A scheduled occurrence of a temporal event. Preferred Term: Scheduled Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**default_condition** | **str** |  | [optional] 
**epoch** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.scheduled_instance import ScheduledInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledInstance from a JSON string
scheduled_instance_instance = ScheduledInstance.from_json(json)
# print the JSON string representation of the object
print(ScheduledInstance.to_json())

# convert the object into a dict
scheduled_instance_dict = scheduled_instance_instance.to_dict()
# create an instance of ScheduledInstance from a dict
scheduled_instance_from_dict = ScheduledInstance.from_dict(scheduled_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


