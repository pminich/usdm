# SyntaxTemplateDictionary

NCI C-Code: C207597 Definition: A reference source that provides a listing of valid parameter names and values used in syntax template text strings. Preferred Term: Syntax Template Dictionary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**parameter_maps** | **List[str]** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.syntax_template_dictionary import SyntaxTemplateDictionary

# TODO update the JSON string below
json = "{}"
# create an instance of SyntaxTemplateDictionary from a JSON string
syntax_template_dictionary_instance = SyntaxTemplateDictionary.from_json(json)
# print the JSON string representation of the object
print SyntaxTemplateDictionary.to_json()

# convert the object into a dict
syntax_template_dictionary_dict = syntax_template_dictionary_instance.to_dict()
# create an instance of SyntaxTemplateDictionary from a dict
syntax_template_dictionary_from_dict = SyntaxTemplateDictionary.from_dict(syntax_template_dictionary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


