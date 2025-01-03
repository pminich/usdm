# SubjectEnrollmentOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | [**QuantityOutput**](QuantityOutput.md) |  | 
**applies_to** | [**GeographicScopeOutput**](GeographicScopeOutput.md) |  | [optional] 
**applies_to_id** | **str** |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.subject_enrollment_output import SubjectEnrollmentOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectEnrollmentOutput from a JSON string
subject_enrollment_output_instance = SubjectEnrollmentOutput.from_json(json)
# print the JSON string representation of the object
print SubjectEnrollmentOutput.to_json()

# convert the object into a dict
subject_enrollment_output_dict = subject_enrollment_output_instance.to_dict()
# create an instance of SubjectEnrollmentOutput from a dict
subject_enrollment_output_from_dict = SubjectEnrollmentOutput.from_dict(subject_enrollment_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


