# NarrativeContentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**text** | **str** |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.narrative_content_item import NarrativeContentItem

# TODO update the JSON string below
json = "{}"
# create an instance of NarrativeContentItem from a JSON string
narrative_content_item_instance = NarrativeContentItem.from_json(json)
# print the JSON string representation of the object
print(NarrativeContentItem.to_json())

# convert the object into a dict
narrative_content_item_dict = narrative_content_item_instance.to_dict()
# create an instance of NarrativeContentItem from a dict
narrative_content_item_from_dict = NarrativeContentItem.from_dict(narrative_content_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


