# StudyTitle

NCI C-Code: C49802 Definition: The sponsor-defined name of the clinical study. Preferred Term: Study Title

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**type** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_title import StudyTitle

# TODO update the JSON string below
json = "{}"
# create an instance of StudyTitle from a JSON string
study_title_instance = StudyTitle.from_json(json)
# print the JSON string representation of the object
print StudyTitle.to_json()

# convert the object into a dict
study_title_dict = study_title_instance.to_dict()
# create an instance of StudyTitle from a dict
study_title_from_dict = StudyTitle.from_dict(study_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


