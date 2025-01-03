# IndicationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**codes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**is_rare_disease** | **bool** |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.indication_input import IndicationInput

# TODO update the JSON string below
json = "{}"
# create an instance of IndicationInput from a JSON string
indication_input_instance = IndicationInput.from_json(json)
# print the JSON string representation of the object
print(IndicationInput.to_json())

# convert the object into a dict
indication_input_dict = indication_input_instance.to_dict()
# create an instance of IndicationInput from a dict
indication_input_from_dict = IndicationInput.from_dict(indication_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


