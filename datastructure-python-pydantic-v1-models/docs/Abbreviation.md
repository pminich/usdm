# Abbreviation

NCI C-Code: C42610 Definition: A set of letters that are drawn from a word or from a sequence of words and that are used for brevity in place of the full word or phrase. (CDISC Glossary) Preferred Term: Abbreviation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**abbreviated_text** | **str** |  | 
**expanded_text** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.abbreviation import Abbreviation

# TODO update the JSON string below
json = "{}"
# create an instance of Abbreviation from a JSON string
abbreviation_instance = Abbreviation.from_json(json)
# print the JSON string representation of the object
print Abbreviation.to_json()

# convert the object into a dict
abbreviation_dict = abbreviation_instance.to_dict()
# create an instance of Abbreviation from a dict
abbreviation_from_dict = Abbreviation.from_dict(abbreviation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


