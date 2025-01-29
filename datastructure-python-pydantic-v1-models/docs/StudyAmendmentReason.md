# StudyAmendmentReason

NCI C-Code: C207457 Definition: The rationale for the change(s) to, or formal clarification of, a protocol. Preferred Term: Study Amendment Reason

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**other_reason** | **str** |  | 
**code** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_amendment_reason import StudyAmendmentReason

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendmentReason from a JSON string
study_amendment_reason_instance = StudyAmendmentReason.from_json(json)
# print the JSON string representation of the object
print StudyAmendmentReason.to_json()

# convert the object into a dict
study_amendment_reason_dict = study_amendment_reason_instance.to_dict()
# create an instance of StudyAmendmentReason from a dict
study_amendment_reason_from_dict = StudyAmendmentReason.from_dict(study_amendment_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


