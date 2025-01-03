# AbbreviationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**abbreviated_text** | **str** |  | 
**expanded_text** | **str** |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.abbreviation_input import AbbreviationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AbbreviationInput from a JSON string
abbreviation_input_instance = AbbreviationInput.from_json(json)
# print the JSON string representation of the object
print(AbbreviationInput.to_json())

# convert the object into a dict
abbreviation_input_dict = abbreviation_input_instance.to_dict()
# create an instance of AbbreviationInput from a dict
abbreviation_input_from_dict = AbbreviationInput.from_dict(abbreviation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


