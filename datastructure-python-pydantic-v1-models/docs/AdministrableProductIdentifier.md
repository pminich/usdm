# AdministrableProductIdentifier

NCI C-Code: CNEW Definition: A sequence of characters used to identify, name, or characterize the administrable product. Preferred Term: Administrable Product Identifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**scope** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.administrable_product_identifier import AdministrableProductIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProductIdentifier from a JSON string
administrable_product_identifier_instance = AdministrableProductIdentifier.from_json(json)
# print the JSON string representation of the object
print AdministrableProductIdentifier.to_json()

# convert the object into a dict
administrable_product_identifier_dict = administrable_product_identifier_instance.to_dict()
# create an instance of AdministrableProductIdentifier from a dict
administrable_product_identifier_from_dict = AdministrableProductIdentifier.from_dict(administrable_product_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


