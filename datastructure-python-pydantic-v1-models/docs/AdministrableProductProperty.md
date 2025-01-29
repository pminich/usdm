# AdministrableProductProperty

NCI C-Code: CNEW Definition: A characteristic from a set of characteristics used to define an administrable product. Preferred Term: Administrable Product Property

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**text** | **str** |  | 
**type** | **str** |  | 
**quantity** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.administrable_product_property import AdministrableProductProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProductProperty from a JSON string
administrable_product_property_instance = AdministrableProductProperty.from_json(json)
# print the JSON string representation of the object
print AdministrableProductProperty.to_json()

# convert the object into a dict
administrable_product_property_dict = administrable_product_property_instance.to_dict()
# create an instance of AdministrableProductProperty from a dict
administrable_product_property_from_dict = AdministrableProductProperty.from_dict(administrable_product_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


