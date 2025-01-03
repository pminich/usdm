# IndicationOutput


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
from openapi_client.models.indication_output import IndicationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of IndicationOutput from a JSON string
indication_output_instance = IndicationOutput.from_json(json)
# print the JSON string representation of the object
print IndicationOutput.to_json()

# convert the object into a dict
indication_output_dict = indication_output_instance.to_dict()
# create an instance of IndicationOutput from a dict
indication_output_from_dict = IndicationOutput.from_dict(indication_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


