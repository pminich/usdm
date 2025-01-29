# StudyDefinitionDocumentVersion

NCI C-Code: CNEW Definition: A representation of a particular edition or snapshot of the study definition document as it exists at a particular point in time. Preferred Term: Study Definition Document Version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **str** |  | 
**status** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**date_values** | **List[str]** |  | [optional] 
**contents** | **List[str]** |  | [optional] 
**children** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_definition_document_version import StudyDefinitionDocumentVersion

# TODO update the JSON string below
json = "{}"
# create an instance of StudyDefinitionDocumentVersion from a JSON string
study_definition_document_version_instance = StudyDefinitionDocumentVersion.from_json(json)
# print the JSON string representation of the object
print(StudyDefinitionDocumentVersion.to_json())

# convert the object into a dict
study_definition_document_version_dict = study_definition_document_version_instance.to_dict()
# create an instance of StudyDefinitionDocumentVersion from a dict
study_definition_document_version_from_dict = StudyDefinitionDocumentVersion.from_dict(study_definition_document_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


