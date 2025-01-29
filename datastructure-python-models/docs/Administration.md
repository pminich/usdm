# Administration

NCI C-Code: C25409 Definition: The act of dispensing, applying, or tendering a product, agent, or therapy. Preferred Term: Administration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**administrable_product** | **str** |  | [optional] 
**route** | **str** |  | [optional] 
**dose** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**duration** | **str** |  | 
**medical_device** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.administration import Administration

# TODO update the JSON string below
json = "{}"
# create an instance of Administration from a JSON string
administration_instance = Administration.from_json(json)
# print the JSON string representation of the object
print(Administration.to_json())

# convert the object into a dict
administration_dict = administration_instance.to_dict()
# create an instance of Administration from a dict
administration_from_dict = Administration.from_dict(administration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


