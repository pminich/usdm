# AdministrationInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | [**AdministrationDurationInput**](AdministrationDurationInput.md) |  | 
**dose** | [**QuantityInput**](QuantityInput.md) |  | 
**route** | [**AliasCode**](AliasCode.md) |  | 
**frequency** | [**AliasCode**](AliasCode.md) |  | 
**administrable_product_id** | **str** |  | [optional] 
**medical_device_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administration_input import AdministrationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrationInput from a JSON string
administration_input_instance = AdministrationInput.from_json(json)
# print the JSON string representation of the object
print AdministrationInput.to_json()

# convert the object into a dict
administration_input_dict = administration_input_instance.to_dict()
# create an instance of AdministrationInput from a dict
administration_input_from_dict = AdministrationInput.from_dict(administration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


