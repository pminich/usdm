# SubstanceInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**codes** | [**List[Code]**](Code.md) |  | [optional] [default to []]
**strengths** | [**List[StrengthInput]**](StrengthInput.md) |  | 
**reference_substance** | [**SubstanceInput**](SubstanceInput.md) |  | [optional] 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.substance_input import SubstanceInput

# TODO update the JSON string below
json = "{}"
# create an instance of SubstanceInput from a JSON string
substance_input_instance = SubstanceInput.from_json(json)
# print the JSON string representation of the object
print SubstanceInput.to_json()

# convert the object into a dict
substance_input_dict = substance_input_instance.to_dict()
# create an instance of SubstanceInput from a dict
substance_input_from_dict = SubstanceInput.from_dict(substance_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


