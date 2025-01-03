# Numerator1


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
from openapi_client.models.numerator1 import Numerator1

# TODO update the JSON string below
json = "{}"
# create an instance of Numerator1 from a JSON string
numerator1_instance = Numerator1.from_json(json)
# print the JSON string representation of the object
print Numerator1.to_json()

# convert the object into a dict
numerator1_dict = numerator1_instance.to_dict()
# create an instance of Numerator1 from a dict
numerator1_from_dict = Numerator1.from_dict(numerator1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


