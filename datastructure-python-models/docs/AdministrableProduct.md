# AdministrableProduct

NCI C-Code: CNEW Definition: Any study product that is formulated and presented in the form that is suitable for administration to a study participant. Preferred Term: Administrable Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**product_designation** | **str** |  | 
**administrable_dose_form** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**pharmacologic_class** | **str** |  | [optional] 
**identifiers** | **List[str]** |  | [optional] 
**properties** | **List[str]** |  | [optional] 
**sourcing** | **str** |  | [optional] 
**ingredients** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.administrable_product import AdministrableProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProduct from a JSON string
administrable_product_instance = AdministrableProduct.from_json(json)
# print the JSON string representation of the object
print(AdministrableProduct.to_json())

# convert the object into a dict
administrable_product_dict = administrable_product_instance.to_dict()
# create an instance of AdministrableProduct from a dict
administrable_product_from_dict = AdministrableProduct.from_dict(administrable_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


