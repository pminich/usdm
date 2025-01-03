# ActivityOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**previous_id** | **str** |  | [optional] 
**next_id** | **str** |  | [optional] 
**child_ids** | **List[str]** |  | [optional] [default to []]
**defined_procedures** | [**List[ProcedureOutput]**](ProcedureOutput.md) |  | [optional] [default to []]
**biomedical_concept_ids** | **List[str]** |  | [optional] [default to []]
**bc_category_ids** | **List[str]** |  | [optional] [default to []]
**bc_surrogate_ids** | **List[str]** |  | [optional] [default to []]
**timeline_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.activity_output import ActivityOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityOutput from a JSON string
activity_output_instance = ActivityOutput.from_json(json)
# print the JSON string representation of the object
print(ActivityOutput.to_json())

# convert the object into a dict
activity_output_dict = activity_output_instance.to_dict()
# create an instance of ActivityOutput from a dict
activity_output_from_dict = ActivityOutput.from_dict(activity_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


