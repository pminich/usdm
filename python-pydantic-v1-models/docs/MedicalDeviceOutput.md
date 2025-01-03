# MedicalDeviceOutput


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
from openapi_client.models.medical_device_output import MedicalDeviceOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalDeviceOutput from a JSON string
medical_device_output_instance = MedicalDeviceOutput.from_json(json)
# print the JSON string representation of the object
print MedicalDeviceOutput.to_json()

# convert the object into a dict
medical_device_output_dict = medical_device_output_instance.to_dict()
# create an instance of MedicalDeviceOutput from a dict
medical_device_output_from_dict = MedicalDeviceOutput.from_dict(medical_device_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


