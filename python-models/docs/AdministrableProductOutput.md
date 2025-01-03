# AdministrableProductOutput


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
**properties** | [**List[AdministrableProductPropertyOutput]**](AdministrableProductPropertyOutput.md) |  | [optional] [default to []]
**identifiers** | [**List[AdministrableProductIdentifier]**](AdministrableProductIdentifier.md) |  | [optional] [default to []]
**ingredients** | [**List[IngredientOutput]**](IngredientOutput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administrable_product_output import AdministrableProductOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrableProductOutput from a JSON string
administrable_product_output_instance = AdministrableProductOutput.from_json(json)
# print the JSON string representation of the object
print(AdministrableProductOutput.to_json())

# convert the object into a dict
administrable_product_output_dict = administrable_product_output_instance.to_dict()
# create an instance of AdministrableProductOutput from a dict
administrable_product_output_from_dict = AdministrableProductOutput.from_dict(administrable_product_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


