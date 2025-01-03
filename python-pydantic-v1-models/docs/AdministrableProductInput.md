# AdministrableProductInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**pharmacologic_class** | [**Code**](Code.md) |  | [optional] 
**administrable_dose_form** | [**AliasCode**](AliasCode.md) |  | 
**product_designation** | [**Code**](Code.md) |  | 
**sourcing** | [**Code**](Code.md) |  | [optional] 
**properties** | [**List[AdministrableProductPropertyInput]**](AdministrableProductPropertyInput.md) |  | [optional] [default to []]
**identifiers** | [**List[AdministrableProductIdentifier]**](AdministrableProductIdentifier.md) |  | [optional] [default to []]
**ingredients** | [**List[IngredientInput]**](IngredientInput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administrable_product_input import AdministrableProductInput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProductInput from a JSON string
administrable_product_input_instance = AdministrableProductInput.from_json(json)
# print the JSON string representation of the object
print AdministrableProductInput.to_json()

# convert the object into a dict
administrable_product_input_dict = administrable_product_input_instance.to_dict()
# create an instance of AdministrableProductInput from a dict
administrable_product_input_from_dict = AdministrableProductInput.from_dict(administrable_product_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


