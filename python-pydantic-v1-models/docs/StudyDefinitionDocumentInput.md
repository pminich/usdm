# StudyDefinitionDocumentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**language** | [**Code**](Code.md) |  | 
**type** | [**Code**](Code.md) |  | 
**template_name** | **str** |  | 
**versions** | [**List[StudyDefinitionDocumentVersionInput]**](StudyDefinitionDocumentVersionInput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_definition_document_input import StudyDefinitionDocumentInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDefinitionDocumentInput from a JSON string
study_definition_document_input_instance = StudyDefinitionDocumentInput.from_json(json)
# print the JSON string representation of the object
print StudyDefinitionDocumentInput.to_json()

# convert the object into a dict
study_definition_document_input_dict = study_definition_document_input_instance.to_dict()
# create an instance of StudyDefinitionDocumentInput from a dict
study_definition_document_input_from_dict = StudyDefinitionDocumentInput.from_dict(study_definition_document_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


