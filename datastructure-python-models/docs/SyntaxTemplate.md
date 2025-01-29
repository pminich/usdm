# SyntaxTemplate

NCI C-Code: C207596 Definition: A standardized pattern used for the arrangement of words and phrases to create well-formed, structured sentences. Preferred Term: Syntax Template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**text** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**dictionary** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.syntax_template import SyntaxTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of SyntaxTemplate from a JSON string
syntax_template_instance = SyntaxTemplate.from_json(json)
# print the JSON string representation of the object
print(SyntaxTemplate.to_json())

# convert the object into a dict
syntax_template_dict = syntax_template_instance.to_dict()
# create an instance of SyntaxTemplate from a dict
syntax_template_from_dict = SyntaxTemplate.from_dict(syntax_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


