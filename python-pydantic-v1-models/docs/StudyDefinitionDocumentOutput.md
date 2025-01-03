# StudyDefinitionDocumentOutput


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
**versions** | [**List[StudyDefinitionDocumentVersionOutput]**](StudyDefinitionDocumentVersionOutput.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_definition_document_output import StudyDefinitionDocumentOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDefinitionDocumentOutput from a JSON string
study_definition_document_output_instance = StudyDefinitionDocumentOutput.from_json(json)
# print the JSON string representation of the object
print StudyDefinitionDocumentOutput.to_json()

# convert the object into a dict
study_definition_document_output_dict = study_definition_document_output_instance.to_dict()
# create an instance of StudyDefinitionDocumentOutput from a dict
study_definition_document_output_from_dict = StudyDefinitionDocumentOutput.from_dict(study_definition_document_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


