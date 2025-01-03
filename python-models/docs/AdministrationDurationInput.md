# AdministrationDurationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**quantity** | [**QuantityInput**](QuantityInput.md) |  | [optional] 
**description** | **str** |  | 
**duration_will_vary** | **bool** |  | 
**reason_duration_will_vary** | **str** |  | 
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.administration_duration_input import AdministrationDurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrationDurationInput from a JSON string
administration_duration_input_instance = AdministrationDurationInput.from_json(json)
# print the JSON string representation of the object
print(AdministrationDurationInput.to_json())

# convert the object into a dict
administration_duration_input_dict = administration_duration_input_instance.to_dict()
# create an instance of AdministrationDurationInput from a dict
administration_duration_input_from_dict = AdministrationDurationInput.from_dict(administration_duration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


