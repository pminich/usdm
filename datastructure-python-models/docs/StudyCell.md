# StudyCell

NCI C-Code: C188810 Definition: A partitioning of a study arm into individual pieces, which are associated with an epoch and any number of sequential elements within that epoch. Preferred Term: Study Design Cell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**arm** | **str** |  | 
**epoch** | **str** |  | 
**elements** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.study_cell import StudyCell

# TODO update the JSON string below
json = "{}"
# create an instance of StudyCell from a JSON string
study_cell_instance = StudyCell.from_json(json)
# print the JSON string representation of the object
print(StudyCell.to_json())

# convert the object into a dict
study_cell_dict = study_cell_instance.to_dict()
# create an instance of StudyCell from a dict
study_cell_from_dict = StudyCell.from_dict(study_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


