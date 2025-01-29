# TransitionRule

NCI C-Code: C82567 Definition: A guide that governs the allocation of subjects to operational options at a discrete decision point or branch (e.g., assignment to a particular arm, discontinuation) within a clinical trial plan. Preferred Term: Transition Rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**text** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transition_rule import TransitionRule

# TODO update the JSON string below
json = "{}"
# create an instance of TransitionRule from a JSON string
transition_rule_instance = TransitionRule.from_json(json)
# print the JSON string representation of the object
print TransitionRule.to_json()

# convert the object into a dict
transition_rule_dict = transition_rule_instance.to_dict()
# create an instance of TransitionRule from a dict
transition_rule_from_dict = TransitionRule.from_dict(transition_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


