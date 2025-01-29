# SubjectEnrollment

NCI C-Code: C37948 Definition: The act of enrolling subjects into a study. The subject will have met the inclusion/exclusion criteria to participate in the trial and will have signed an informed consent form. (CDISC Glossary) Preferred Term: Subject Enrollment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**applies_to** | **str** |  | [optional] 
**quantity** | **str** |  | 
**applies_to_id** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.subject_enrollment import SubjectEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectEnrollment from a JSON string
subject_enrollment_instance = SubjectEnrollment.from_json(json)
# print the JSON string representation of the object
print(SubjectEnrollment.to_json())

# convert the object into a dict
subject_enrollment_dict = subject_enrollment_instance.to_dict()
# create an instance of SubjectEnrollment from a dict
subject_enrollment_from_dict = SubjectEnrollment.from_dict(subject_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


