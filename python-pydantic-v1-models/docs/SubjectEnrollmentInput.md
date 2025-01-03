# SubjectEnrollmentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | [**QuantityInput**](QuantityInput.md) |  | 
**applies_to** | [**GeographicScopeInput**](GeographicScopeInput.md) |  | [optional] 
**applies_to_id** | **str** |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.subject_enrollment_input import SubjectEnrollmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectEnrollmentInput from a JSON string
subject_enrollment_input_instance = SubjectEnrollmentInput.from_json(json)
# print the JSON string representation of the object
print SubjectEnrollmentInput.to_json()

# convert the object into a dict
subject_enrollment_input_dict = subject_enrollment_input_instance.to_dict()
# create an instance of SubjectEnrollmentInput from a dict
subject_enrollment_input_from_dict = SubjectEnrollmentInput.from_dict(subject_enrollment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


