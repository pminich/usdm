# StudyAmendmentImpactInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**Code**](Code.md) |  | 
**text** | **str** |  | 
**is_substantial** | **bool** |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_amendment_impact_input import StudyAmendmentImpactInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendmentImpactInput from a JSON string
study_amendment_impact_input_instance = StudyAmendmentImpactInput.from_json(json)
# print the JSON string representation of the object
print(StudyAmendmentImpactInput.to_json())

# convert the object into a dict
study_amendment_impact_input_dict = study_amendment_impact_input_instance.to_dict()
# create an instance of StudyAmendmentImpactInput from a dict
study_amendment_impact_input_from_dict = StudyAmendmentImpactInput.from_dict(study_amendment_impact_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


