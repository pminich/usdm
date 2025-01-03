# BiomedicalConceptSurrogateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.biomedical_concept_surrogate_input import BiomedicalConceptSurrogateInput

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptSurrogateInput from a JSON string
biomedical_concept_surrogate_input_instance = BiomedicalConceptSurrogateInput.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptSurrogateInput.to_json()

# convert the object into a dict
biomedical_concept_surrogate_input_dict = biomedical_concept_surrogate_input_instance.to_dict()
# create an instance of BiomedicalConceptSurrogateInput from a dict
biomedical_concept_surrogate_input_from_dict = BiomedicalConceptSurrogateInput.from_dict(biomedical_concept_surrogate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


