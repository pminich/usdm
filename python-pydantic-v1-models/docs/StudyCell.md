# StudyCell


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**arm_id** | **str** |  | 
**epoch_id** | **str** |  | 
**element_ids** | **List[str]** |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.study_cell import StudyCell

# TODO update the JSON string below
json = "{}"
# create an instance of StudyCell from a JSON string
study_cell_instance = StudyCell.from_json(json)
# print the JSON string representation of the object
print StudyCell.to_json()

# convert the object into a dict
study_cell_dict = study_cell_instance.to_dict()
# create an instance of StudyCell from a dict
study_cell_from_dict = StudyCell.from_dict(study_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


