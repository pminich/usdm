# Numerator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **float** |  | 
**unit** | [**AliasCode**](AliasCode.md) |  | [optional] 
**instance_type** | **str** |  | 
**min_value** | **float** |  | 
**max_value** | **float** |  | 
**is_approximate** | **bool** |  | 

## Example

```python
from openapi_client.models.numerator import Numerator

# TODO update the JSON string below
json = "{}"
# create an instance of Numerator from a JSON string
numerator_instance = Numerator.from_json(json)
# print the JSON string representation of the object
print Numerator.to_json()

# convert the object into a dict
numerator_dict = numerator_instance.to_dict()
# create an instance of Numerator from a dict
numerator_from_dict = Numerator.from_dict(numerator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


