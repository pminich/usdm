# StudyElementInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**transition_start_rule** | [**TransitionRule**](TransitionRule.md) |  | [optional] 
**transition_end_rule** | [**TransitionRule**](TransitionRule.md) |  | [optional] 
**study_intervention_ids** | **List[Optional[str]]** |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_element_input import StudyElementInput

# TODO update the JSON string below
json = "{}"
# create an instance of StudyElementInput from a JSON string
study_element_input_instance = StudyElementInput.from_json(json)
# print the JSON string representation of the object
print(StudyElementInput.to_json())

# convert the object into a dict
study_element_input_dict = study_element_input_instance.to_dict()
# create an instance of StudyElementInput from a dict
study_element_input_from_dict = StudyElementInput.from_dict(study_element_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


