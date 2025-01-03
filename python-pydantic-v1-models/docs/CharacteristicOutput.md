# CharacteristicOutput


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
from openapi_client.models.characteristic_output import CharacteristicOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CharacteristicOutput from a JSON string
characteristic_output_instance = CharacteristicOutput.from_json(json)
# print the JSON string representation of the object
print CharacteristicOutput.to_json()

# convert the object into a dict
characteristic_output_dict = characteristic_output_instance.to_dict()
# create an instance of CharacteristicOutput from a dict
characteristic_output_from_dict = CharacteristicOutput.from_dict(characteristic_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


