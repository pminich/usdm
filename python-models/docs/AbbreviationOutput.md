# AbbreviationOutput


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
from openapi_client.models.abbreviation_output import AbbreviationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AbbreviationOutput from a JSON string
abbreviation_output_instance = AbbreviationOutput.from_json(json)
# print the JSON string representation of the object
print(AbbreviationOutput.to_json())

# convert the object into a dict
abbreviation_output_dict = abbreviation_output_instance.to_dict()
# create an instance of AbbreviationOutput from a dict
abbreviation_output_from_dict = AbbreviationOutput.from_dict(abbreviation_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


