# ConditionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**text** | **str** |  | 
**dictionary_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 
**context_ids** | **List[str]** |  | [optional] [default to []]
**applies_to_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from openapi_client.models.condition_output import ConditionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionOutput from a JSON string
condition_output_instance = ConditionOutput.from_json(json)
# print the JSON string representation of the object
print(ConditionOutput.to_json())

# convert the object into a dict
condition_output_dict = condition_output_instance.to_dict()
# create an instance of ConditionOutput from a dict
condition_output_from_dict = ConditionOutput.from_dict(condition_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


