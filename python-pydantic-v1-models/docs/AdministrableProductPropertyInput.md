# AdministrableProductPropertyInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**text** | **str** |  | 
**type** | [**Code**](Code.md) |  | 
**quantity** | [**QuantityInput**](QuantityInput.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administrable_product_property_input import AdministrableProductPropertyInput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProductPropertyInput from a JSON string
administrable_product_property_input_instance = AdministrableProductPropertyInput.from_json(json)
# print the JSON string representation of the object
print AdministrableProductPropertyInput.to_json()

# convert the object into a dict
administrable_product_property_input_dict = administrable_product_property_input_instance.to_dict()
# create an instance of AdministrableProductPropertyInput from a dict
administrable_product_property_input_from_dict = AdministrableProductPropertyInput.from_dict(administrable_product_property_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


