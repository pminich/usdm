# StudyAmendmentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**number** | **str** |  | 
**summary** | **str** |  | 
**primary_reason** | [**StudyAmendmentReason**](StudyAmendmentReason.md) |  | 
**secondary_reasons** | [**List[StudyAmendmentReason]**](StudyAmendmentReason.md) |  | [optional] [default to []]
**changes** | [**List[StudyChange]**](StudyChange.md) |  | 
**impacts** | [**List[StudyAmendmentImpactInput]**](StudyAmendmentImpactInput.md) |  | [optional] [default to []]
**geographic_scopes** | [**List[GeographicScopeInput]**](GeographicScopeInput.md) |  | 
**enrollments** | [**List[SubjectEnrollmentInput]**](SubjectEnrollmentInput.md) |  | [optional] [default to []]
**date_values** | [**List[GovernanceDateInput]**](GovernanceDateInput.md) |  | [optional] [default to []]
**previous_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_amendment_input import StudyAmendmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendmentInput from a JSON string
study_amendment_input_instance = StudyAmendmentInput.from_json(json)
# print the JSON string representation of the object
print StudyAmendmentInput.to_json()

# convert the object into a dict
study_amendment_input_dict = study_amendment_input_instance.to_dict()
# create an instance of StudyAmendmentInput from a dict
study_amendment_input_from_dict = StudyAmendmentInput.from_dict(study_amendment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


