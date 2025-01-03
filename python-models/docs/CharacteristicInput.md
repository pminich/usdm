# CharacteristicInput


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

## Example

```python
from openapi_client.models.characteristic_input import CharacteristicInput

# TODO update the JSON string below
json = "{}"
# create an instance of CharacteristicInput from a JSON string
characteristic_input_instance = CharacteristicInput.from_json(json)
# print the JSON string representation of the object
print(CharacteristicInput.to_json())

# convert the object into a dict
characteristic_input_dict = characteristic_input_instance.to_dict()
# create an instance of CharacteristicInput from a dict
characteristic_input_from_dict = CharacteristicInput.from_dict(characteristic_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


