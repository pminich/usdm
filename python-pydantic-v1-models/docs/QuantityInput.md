# QuantityInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **float** |  | 
**unit** | [**AliasCode**](AliasCode.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.quantity_input import QuantityInput

# TODO update the JSON string below
json = "{}"
# create an instance of QuantityInput from a JSON string
quantity_input_instance = QuantityInput.from_json(json)
# print the JSON string representation of the object
print QuantityInput.to_json()

# convert the object into a dict
quantity_input_dict = quantity_input_instance.to_dict()
# create an instance of QuantityInput from a dict
quantity_input_from_dict = QuantityInput.from_dict(quantity_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


