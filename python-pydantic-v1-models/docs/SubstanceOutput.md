# SubstanceOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**codes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**strengths** | [**List[StrengthOutput]**](StrengthOutput.md) |  | 
**reference_substance** | [**SubstanceOutput**](SubstanceOutput.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.substance_output import SubstanceOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SubstanceOutput from a JSON string
substance_output_instance = SubstanceOutput.from_json(json)
# print the JSON string representation of the object
print SubstanceOutput.to_json()

# convert the object into a dict
substance_output_dict = substance_output_instance.to_dict()
# create an instance of SubstanceOutput from a dict
substance_output_from_dict = SubstanceOutput.from_dict(substance_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


