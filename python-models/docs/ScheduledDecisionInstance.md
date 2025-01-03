# ScheduledDecisionInstance


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
**condition_assignments** | [**List[ConditionAssignment]**](ConditionAssignment.md) |  | 

## Example

```python
from openapi_client.models.scheduled_decision_instance import ScheduledDecisionInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledDecisionInstance from a JSON string
scheduled_decision_instance_instance = ScheduledDecisionInstance.from_json(json)
# print the JSON string representation of the object
print(ScheduledDecisionInstance.to_json())

# convert the object into a dict
scheduled_decision_instance_dict = scheduled_decision_instance_instance.to_dict()
# create an instance of ScheduledDecisionInstance from a dict
scheduled_decision_instance_from_dict = ScheduledDecisionInstance.from_dict(scheduled_decision_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


