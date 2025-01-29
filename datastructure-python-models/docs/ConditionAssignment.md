# ConditionAssignment

NCI C-Code: C201335 Definition: An allotting or appointment to a condition or set of conditions that are to be met in order to make a logical decision. Preferred Term: Condition Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**condition** | **str** |  | 
**condition_target** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.condition_assignment import ConditionAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionAssignment from a JSON string
condition_assignment_instance = ConditionAssignment.from_json(json)
# print the JSON string representation of the object
print(ConditionAssignment.to_json())

# convert the object into a dict
condition_assignment_dict = condition_assignment_instance.to_dict()
# create an instance of ConditionAssignment from a dict
condition_assignment_from_dict = ConditionAssignment.from_dict(condition_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


