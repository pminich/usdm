# NarrativeContent

NCI C-Code: C207592 Definition: The container that holds an instance of unstructured text and which may include objects such as tables, figures, and images. Preferred Term: Narrative Content

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**section_number** | **str** |  | 
**section_title** | **str** |  | 
**display_section_title** | **str** |  | 
**display_section_number** | **str** |  | 
**content_item** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**children** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.narrative_content import NarrativeContent

# TODO update the JSON string below
json = "{}"
# create an instance of NarrativeContent from a JSON string
narrative_content_instance = NarrativeContent.from_json(json)
# print the JSON string representation of the object
print NarrativeContent.to_json()

# convert the object into a dict
narrative_content_dict = narrative_content_instance.to_dict()
# create an instance of NarrativeContent from a dict
narrative_content_from_dict = NarrativeContent.from_dict(narrative_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


