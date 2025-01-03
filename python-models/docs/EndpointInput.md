# EndpointInput


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
**purpose** | **str** |  | 
**level** | [**Code**](Code.md) |  | 

## Example

```python
from openapi_client.models.endpoint_input import EndpointInput

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointInput from a JSON string
endpoint_input_instance = EndpointInput.from_json(json)
# print the JSON string representation of the object
print(EndpointInput.to_json())

# convert the object into a dict
endpoint_input_dict = endpoint_input_instance.to_dict()
# create an instance of EndpointInput from a dict
endpoint_input_from_dict = EndpointInput.from_dict(endpoint_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


