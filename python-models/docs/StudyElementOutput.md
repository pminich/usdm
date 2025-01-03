# StudyElementOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**transition_start_rule** | [**TransitionRule**](TransitionRule.md) |  | [optional] 
**transition_end_rule** | [**TransitionRule**](TransitionRule.md) |  | [optional] 
**study_intervention_ids** | **List[str]** |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_element_output import StudyElementOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyElementOutput from a JSON string
study_element_output_instance = StudyElementOutput.from_json(json)
# print the JSON string representation of the object
print(StudyElementOutput.to_json())

# convert the object into a dict
study_element_output_dict = study_element_output_instance.to_dict()
# create an instance of StudyElementOutput from a dict
study_element_output_from_dict = StudyElementOutput.from_dict(study_element_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


