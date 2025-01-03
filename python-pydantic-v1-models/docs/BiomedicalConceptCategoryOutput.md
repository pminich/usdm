# BiomedicalConceptCategoryOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**child_ids** | **List[str]** |  | [optional] [default to []]
**member_ids** | **List[str]** |  | [optional] [default to []]
**code** | [**AliasCode**](AliasCode.md) |  | [optional] 
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.biomedical_concept_category_output import BiomedicalConceptCategoryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BiomedicalConceptCategoryOutput from a JSON string
biomedical_concept_category_output_instance = BiomedicalConceptCategoryOutput.from_json(json)
# print the JSON string representation of the object
print BiomedicalConceptCategoryOutput.to_json()

# convert the object into a dict
biomedical_concept_category_output_dict = biomedical_concept_category_output_instance.to_dict()
# create an instance of BiomedicalConceptCategoryOutput from a dict
biomedical_concept_category_output_from_dict = BiomedicalConceptCategoryOutput.from_dict(biomedical_concept_category_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


