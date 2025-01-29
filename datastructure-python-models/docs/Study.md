# Study

NCI C-Code: C15206 Definition: A clinical study involves research using human volunteers (also called participants) that is intended to add to medical knowledge. There are two main types of clinical studies: clinical trials (also called interventional studies) and observational studies. (CDISC Glossary) Preferred Term: Clinical Study

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**versions** | **List[str]** |  | [optional] 
**documented_by** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study import Study

# TODO update the JSON string below
json = "{}"
# create an instance of Study from a JSON string
study_instance = Study.from_json(json)
# print the JSON string representation of the object
print(Study.to_json())

# convert the object into a dict
study_dict = study_instance.to_dict()
# create an instance of Study from a dict
study_from_dict = Study.from_dict(study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


