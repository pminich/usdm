# IntercurrentEvent

NCI C-Code: C188815 Definition: An event(s) occurring after treatment initiation that affects either the interpretation or the existence of the measurements associated with the clinical question of interest. (ICH E9 Addendum on Estimands) Preferred Term: Intercurrent Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**text** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**dictionary** | **str** |  | [optional] 
**strategy** | **str** |  | 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.intercurrent_event import IntercurrentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IntercurrentEvent from a JSON string
intercurrent_event_instance = IntercurrentEvent.from_json(json)
# print the JSON string representation of the object
print IntercurrentEvent.to_json()

# convert the object into a dict
intercurrent_event_dict = intercurrent_event_instance.to_dict()
# create an instance of IntercurrentEvent from a dict
intercurrent_event_from_dict = IntercurrentEvent.from_dict(intercurrent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


