# Indication

NCI C-Code: C41184 Definition: The disease or condition the intervention will diagnose, treat, prevent, cure, or mitigate. Preferred Term: Disease/Condition Indication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**is_rare_disease** | **str** |  | 
**codes** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.indication import Indication

# TODO update the JSON string below
json = "{}"
# create an instance of Indication from a JSON string
indication_instance = Indication.from_json(json)
# print the JSON string representation of the object
print(Indication.to_json())

# convert the object into a dict
indication_dict = indication_instance.to_dict()
# create an instance of Indication from a dict
indication_from_dict = Indication.from_dict(indication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


