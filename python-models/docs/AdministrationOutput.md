# AdministrationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | [**AdministrationDurationOutput**](AdministrationDurationOutput.md) |  | 
**dose** | [**QuantityOutput**](QuantityOutput.md) |  | 
**route** | [**AliasCode**](AliasCode.md) |  | 
**frequency** | [**AliasCode**](AliasCode.md) |  | 
**administrable_product_id** | **str** |  | [optional] 
**medical_device_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administration_output import AdministrationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrationOutput from a JSON string
administration_output_instance = AdministrationOutput.from_json(json)
# print the JSON string representation of the object
print(AdministrationOutput.to_json())

# convert the object into a dict
administration_output_dict = administration_output_instance.to_dict()
# create an instance of AdministrationOutput from a dict
administration_output_from_dict = AdministrationOutput.from_dict(administration_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


