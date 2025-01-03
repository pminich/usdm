# StudyAmendmentImpactOutput


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
from openapi_client.models.study_amendment_impact_output import StudyAmendmentImpactOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendmentImpactOutput from a JSON string
study_amendment_impact_output_instance = StudyAmendmentImpactOutput.from_json(json)
# print the JSON string representation of the object
print StudyAmendmentImpactOutput.to_json()

# convert the object into a dict
study_amendment_impact_output_dict = study_amendment_impact_output_instance.to_dict()
# create an instance of StudyAmendmentImpactOutput from a dict
study_amendment_impact_output_from_dict = StudyAmendmentImpactOutput.from_dict(study_amendment_impact_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


