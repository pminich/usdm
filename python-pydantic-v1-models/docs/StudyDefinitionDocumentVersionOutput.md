# StudyDefinitionDocumentVersionOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **str** |  | 
**status** | [**Code**](Code.md) |  | 
**date_values** | [**List[GovernanceDateOutput]**](GovernanceDateOutput.md) |  | [optional] [default to []]
**contents** | [**List[NarrativeContent]**](NarrativeContent.md) |  | [optional] [default to []]
**child_ids** | **List[str]** |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_definition_document_version_output import StudyDefinitionDocumentVersionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDefinitionDocumentVersionOutput from a JSON string
study_definition_document_version_output_instance = StudyDefinitionDocumentVersionOutput.from_json(json)
# print the JSON string representation of the object
print StudyDefinitionDocumentVersionOutput.to_json()

# convert the object into a dict
study_definition_document_version_output_dict = study_definition_document_version_output_instance.to_dict()
# create an instance of StudyDefinitionDocumentVersionOutput from a dict
study_definition_document_version_output_from_dict = StudyDefinitionDocumentVersionOutput.from_dict(study_definition_document_version_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


