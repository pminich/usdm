# BiomedicalConceptOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**synonyms** | **List[str]** |  | [optional] [default to []]
**reference** | **str** |  | 
**properties** | [**List[BiomedicalConceptPropertyOutput]**](BiomedicalConceptPropertyOutput.md) |  | [optional] [default to []]
**code** | [**AliasCode**](AliasCode.md) |  | 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.biomedical_concept_output import BiomedicalConceptOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptOutput from a JSON string
biomedical_concept_output_instance = BiomedicalConceptOutput.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptOutput.to_json()

# convert the object into a dict
biomedical_concept_output_dict = biomedical_concept_output_instance.to_dict()
# create an instance of BiomedicalConceptOutput from a dict
biomedical_concept_output_from_dict = BiomedicalConceptOutput.from_dict(biomedical_concept_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


