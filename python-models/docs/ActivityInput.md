# ActivityInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**previous_id** | **str** |  | [optional] 
**next_id** | **str** |  | [optional] 
**child_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**defined_procedures** | [**List[ProcedureInput]**](ProcedureInput.md) |  | [optional] [default to []]
**biomedical_concept_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**bc_category_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**bc_surrogate_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**timeline_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.activity_input import ActivityInput

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityInput from a JSON string
activity_input_instance = ActivityInput.from_json(json)
# print the JSON string representation of the object
print(ActivityInput.to_json())

# convert the object into a dict
activity_input_dict = activity_input_instance.to_dict()
# create an instance of ActivityInput from a dict
activity_input_from_dict = ActivityInput.from_dict(activity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


