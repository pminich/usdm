# StudyAmendmentOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**number** | **str** |  | 
**summary** | **str** |  | 
**primary_reason** | [**StudyAmendmentReason**](StudyAmendmentReason.md) |  | 
**secondary_reasons** | [**List[StudyAmendmentReason]**](StudyAmendmentReason.md) |  | [optional] [default to []]
**changes** | [**List[StudyChange]**](StudyChange.md) |  | 
**impacts** | [**List[StudyAmendmentImpactOutput]**](StudyAmendmentImpactOutput.md) |  | [optional] [default to []]
**geographic_scopes** | [**List[GeographicScopeOutput]**](GeographicScopeOutput.md) |  | 
**enrollments** | [**List[SubjectEnrollmentOutput]**](SubjectEnrollmentOutput.md) |  | [optional] [default to []]
**date_values** | [**List[GovernanceDateOutput]**](GovernanceDateOutput.md) |  | [optional] [default to []]
**previous_id** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_amendment_output import StudyAmendmentOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendmentOutput from a JSON string
study_amendment_output_instance = StudyAmendmentOutput.from_json(json)
# print the JSON string representation of the object
print(StudyAmendmentOutput.to_json())

# convert the object into a dict
study_amendment_output_dict = study_amendment_output_instance.to_dict()
# create an instance of StudyAmendmentOutput from a dict
study_amendment_output_from_dict = StudyAmendmentOutput.from_dict(study_amendment_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


