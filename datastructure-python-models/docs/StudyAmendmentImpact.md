# StudyAmendmentImpact

NCI C-Code: CNEW Definition: The effect or consequence of an amendment on some aspect of the study. Preferred Term: Study Amendment Impact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**is_substantial** | **str** |  | 
**type** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_amendment_impact import StudyAmendmentImpact

# TODO update the JSON string below
json = "{}"
# create an instance of StudyAmendmentImpact from a JSON string
study_amendment_impact_instance = StudyAmendmentImpact.from_json(json)
# print the JSON string representation of the object
print(StudyAmendmentImpact.to_json())

# convert the object into a dict
study_amendment_impact_dict = study_amendment_impact_instance.to_dict()
# create an instance of StudyAmendmentImpact from a dict
study_amendment_impact_from_dict = StudyAmendmentImpact.from_dict(study_amendment_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


