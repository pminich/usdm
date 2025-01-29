# StudyEpoch

NCI C-Code: C71738 Definition: A named time period defined in the protocol, wherein a study activity is specified and unchanging throughout the interval, to support a study-specific purpose. Preferred Term: Study Epoch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**type** | **str** |  | 
**notes** | **List[str]** |  | [optional] 
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_epoch import StudyEpoch

# TODO update the JSON string below
json = "{}"
# create an instance of StudyEpoch from a JSON string
study_epoch_instance = StudyEpoch.from_json(json)
# print the JSON string representation of the object
print StudyEpoch.to_json()

# convert the object into a dict
study_epoch_dict = study_epoch_instance.to_dict()
# create an instance of StudyEpoch from a dict
study_epoch_from_dict = StudyEpoch.from_dict(study_epoch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


