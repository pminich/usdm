# Masking

NCI C-Code: C191278 Definition: The mechanism used to obscure the distinctive characteristics of the study intervention or procedure to make it indistinguishable from a comparator. (CDISC Glossary) Preferred Term: Masking

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.masking import Masking

# TODO update the JSON string below
json = "{}"
# create an instance of Masking from a JSON string
masking_instance = Masking.from_json(json)
# print the JSON string representation of the object
print Masking.to_json()

# convert the object into a dict
masking_dict = masking_instance.to_dict()
# create an instance of Masking from a dict
masking_from_dict = Masking.from_dict(masking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


