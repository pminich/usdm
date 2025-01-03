# StudyIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**scope_id** | **str** |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_identifier import StudyIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of StudyIdentifier from a JSON string
study_identifier_instance = StudyIdentifier.from_json(json)
# print the JSON string representation of the object
print StudyIdentifier.to_json()

# convert the object into a dict
study_identifier_dict = study_identifier_instance.to_dict()
# create an instance of StudyIdentifier from a dict
study_identifier_from_dict = StudyIdentifier.from_dict(study_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


