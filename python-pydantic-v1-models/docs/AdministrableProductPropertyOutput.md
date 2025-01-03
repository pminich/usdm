# AdministrableProductPropertyOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**text** | **str** |  | 
**type** | [**Code**](Code.md) |  | 
**quantity** | [**QuantityOutput**](QuantityOutput.md) |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administrable_product_property_output import AdministrableProductPropertyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProductPropertyOutput from a JSON string
administrable_product_property_output_instance = AdministrableProductPropertyOutput.from_json(json)
# print the JSON string representation of the object
print AdministrableProductPropertyOutput.to_json()

# convert the object into a dict
administrable_product_property_output_dict = administrable_product_property_output_instance.to_dict()
# create an instance of AdministrableProductPropertyOutput from a dict
administrable_product_property_output_from_dict = AdministrableProductPropertyOutput.from_dict(administrable_product_property_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


