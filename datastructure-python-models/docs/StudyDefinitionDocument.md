# StudyDefinitionDocument

NCI C-Code: CNEW Definition: Any physical or electronic document that is related to defining a study or part of a study. Preferred Term: Study Definition Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**template_name** | **str** |  | 
**language** | **str** |  | 
**type** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**versions** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_definition_document import StudyDefinitionDocument

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDefinitionDocument from a JSON string
study_definition_document_instance = StudyDefinitionDocument.from_json(json)
# print the JSON string representation of the object
print(StudyDefinitionDocument.to_json())

# convert the object into a dict
study_definition_document_dict = study_definition_document_instance.to_dict()
# create an instance of StudyDefinitionDocument from a dict
study_definition_document_from_dict = StudyDefinitionDocument.from_dict(study_definition_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


