# BiomedicalConceptSurrogateOutput


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
from openapi_client.models.biomedical_concept_surrogate_output import BiomedicalConceptSurrogateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptSurrogateOutput from a JSON string
biomedical_concept_surrogate_output_instance = BiomedicalConceptSurrogateOutput.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptSurrogateOutput.to_json()

# convert the object into a dict
biomedical_concept_surrogate_output_dict = biomedical_concept_surrogate_output_instance.to_dict()
# create an instance of BiomedicalConceptSurrogateOutput from a dict
biomedical_concept_surrogate_output_from_dict = BiomedicalConceptSurrogateOutput.from_dict(biomedical_concept_surrogate_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


