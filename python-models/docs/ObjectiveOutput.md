# ObjectiveOutput


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
**level** | [**Code**](Code.md) |  | 
**endpoints** | [**List[EndpointOutput]**](EndpointOutput.md) |  | [optional] [default to []]

## Example

```python
from openapi_client.models.objective_output import ObjectiveOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectiveOutput from a JSON string
objective_output_instance = ObjectiveOutput.from_json(json)
# print the JSON string representation of the object
print(ObjectiveOutput.to_json())

# convert the object into a dict
objective_output_dict = objective_output_instance.to_dict()
# create an instance of ObjectiveOutput from a dict
objective_output_from_dict = ObjectiveOutput.from_dict(objective_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


