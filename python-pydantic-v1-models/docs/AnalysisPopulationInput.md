# AnalysisPopulationInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**text** | **str** |  | 
**subset_of_ids** | **List[str]** |  | [optional] [default to []]
**notes** | [**List[CommentAnnotation]**](CommentAnnotation.md) |  | [optional] [default to []]
**instance_type** | **str** |  | 

## Example

```python
from openapi_client.models.analysis_population_input import AnalysisPopulationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisPopulationInput from a JSON string
analysis_population_input_instance = AnalysisPopulationInput.from_json(json)
# print the JSON string representation of the object
print AnalysisPopulationInput.to_json()

# convert the object into a dict
analysis_population_input_dict = analysis_population_input_instance.to_dict()
# create an instance of AnalysisPopulationInput from a dict
analysis_population_input_from_dict = AnalysisPopulationInput.from_dict(analysis_population_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


