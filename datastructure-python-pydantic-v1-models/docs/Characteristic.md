# Characteristic

NCI C-Code: C25447 Definition: The distinguishing qualities or prominent aspects of an entity. Preferred Term: Characteristic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**text** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**dictionary** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.characteristic import Characteristic

# TODO update the JSON string below
json = "{}"
# create an instance of Characteristic from a JSON string
characteristic_instance = Characteristic.from_json(json)
# print the JSON string representation of the object
print Characteristic.to_json()

# convert the object into a dict
characteristic_dict = characteristic_instance.to_dict()
# create an instance of Characteristic from a dict
characteristic_from_dict = Characteristic.from_dict(characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


