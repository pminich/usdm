# ObjectiveInput


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
**endpoints** | [**List[EndpointInput]**](EndpointInput.md) |  | [optional] [default to []]

## Example

```python
from openapi_client.models.objective_input import ObjectiveInput

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectiveInput from a JSON string
objective_input_instance = ObjectiveInput.from_json(json)
# print the JSON string representation of the object
print(ObjectiveInput.to_json())

# convert the object into a dict
objective_input_dict = objective_input_instance.to_dict()
# create an instance of ObjectiveInput from a dict
objective_input_from_dict = ObjectiveInput.from_dict(objective_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


