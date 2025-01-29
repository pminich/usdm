# ScheduledDecisionInstance

NCI C-Code: C201351 Definition: A scheduled occurrence of a decision event. Preferred Term: Scheduled Decision Instance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**default_condition** | **str** |  | [optional] 
**epoch** | **str** |  | [optional] 
**condition_assignments** | **List[str]** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.scheduled_decision_instance import ScheduledDecisionInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledDecisionInstance from a JSON string
scheduled_decision_instance_instance = ScheduledDecisionInstance.from_json(json)
# print the JSON string representation of the object
print ScheduledDecisionInstance.to_json()

# convert the object into a dict
scheduled_decision_instance_dict = scheduled_decision_instance_instance.to_dict()
# create an instance of ScheduledDecisionInstance from a dict
scheduled_decision_instance_from_dict = ScheduledDecisionInstance.from_dict(scheduled_decision_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


