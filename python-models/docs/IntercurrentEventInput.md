# IntercurrentEventInput


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
**strategy** | **str** |  | 

## Example

```python
from openapi_client.models.intercurrent_event_input import IntercurrentEventInput

# TODO update the JSON string below
json = "{}"
# create an instance of IntercurrentEventInput from a JSON string
intercurrent_event_input_instance = IntercurrentEventInput.from_json(json)
# print the JSON string representation of the object
print(IntercurrentEventInput.to_json())

# convert the object into a dict
intercurrent_event_input_dict = intercurrent_event_input_instance.to_dict()
# create an instance of IntercurrentEventInput from a dict
intercurrent_event_input_from_dict = IntercurrentEventInput.from_dict(intercurrent_event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


