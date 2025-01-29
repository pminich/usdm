# Substance

NCI C-Code: C45306 Definition: Any matter of defined composition that has discrete existence, whose origin may be biological, mineral or chemical. Preferred Term: Substance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**codes** | **List[str]** |  | [optional] 
**strengths** | **List[str]** |  | 
**reference_substance** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.substance import Substance

# TODO update the JSON string below
json = "{}"
# create an instance of Substance from a JSON string
substance_instance = Substance.from_json(json)
# print the JSON string representation of the object
print Substance.to_json()

# convert the object into a dict
substance_dict = substance_instance.to_dict()
# create an instance of Substance from a dict
substance_from_dict = Substance.from_dict(substance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


