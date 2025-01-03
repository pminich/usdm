# MedicalDeviceInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hardware_version** | **str** |  | [optional] 
**software_version** | **str** |  | [optional] 
**embedded_product_id** | **str** |  | [optional] 
**sourcing** | [**Code**](Code.md) |  | [optional] 
**identifiers** | [**List[MedicalDeviceIdentifier]**](MedicalDeviceIdentifier.md) |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.medical_device_input import MedicalDeviceInput

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalDeviceInput from a JSON string
medical_device_input_instance = MedicalDeviceInput.from_json(json)
# print the JSON string representation of the object
print MedicalDeviceInput.to_json()

# convert the object into a dict
medical_device_input_dict = medical_device_input_instance.to_dict()
# create an instance of MedicalDeviceInput from a dict
medical_device_input_from_dict = MedicalDeviceInput.from_dict(medical_device_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


