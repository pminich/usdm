# AnalysisPopulationOutput


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
from openapi_client.models.analysis_population_output import AnalysisPopulationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisPopulationOutput from a JSON string
analysis_population_output_instance = AnalysisPopulationOutput.from_json(json)
# print the JSON string representation of the object
print AnalysisPopulationOutput.to_json()

# convert the object into a dict
analysis_population_output_dict = analysis_population_output_instance.to_dict()
# create an instance of AnalysisPopulationOutput from a dict
analysis_population_output_from_dict = AnalysisPopulationOutput.from_dict(analysis_population_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


