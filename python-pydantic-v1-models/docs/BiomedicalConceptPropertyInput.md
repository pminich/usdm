# BiomedicalConceptPropertyInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**is_required** | **bool** |  | 
**is_enabled** | **bool** |  | 
**datatype** | **str** |  | 
**response_codes** | [**List[ResponseCode]**](ResponseCode.md) |  | [optional] [default to []]
**code** | [**AliasCode**](AliasCode.md) |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.biomedical_concept_property_input import BiomedicalConceptPropertyInput

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptPropertyInput from a JSON string
biomedical_concept_property_input_instance = BiomedicalConceptPropertyInput.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptPropertyInput.to_json()

# convert the object into a dict
biomedical_concept_property_input_dict = biomedical_concept_property_input_instance.to_dict()
# create an instance of BiomedicalConceptPropertyInput from a dict
biomedical_concept_property_input_from_dict = BiomedicalConceptPropertyInput.from_dict(biomedical_concept_property_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


