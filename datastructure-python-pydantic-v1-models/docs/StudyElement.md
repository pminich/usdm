# StudyElement

NCI C-Code: C142735 Definition: A basic building block for time within a clinical study comprising the following characteristics: a description of what happens to the subject during the element; a definition of the start of the element; a rule for ending the element. Preferred Term: Study Design Element

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**transition_end_rule** | **str** |  | [optional] 
**study_interventions** | **List[str]** |  | [optional] 
**transition_start_rule** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_element import StudyElement

# TODO update the JSON string below
json = "{}"
# create an instance of StudyElement from a JSON string
study_element_instance = StudyElement.from_json(json)
# print the JSON string representation of the object
print StudyElement.to_json()

# convert the object into a dict
study_element_dict = study_element_instance.to_dict()
# create an instance of StudyElement from a dict
study_element_from_dict = StudyElement.from_dict(study_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


