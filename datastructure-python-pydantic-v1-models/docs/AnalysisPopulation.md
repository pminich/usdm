# AnalysisPopulation

NCI C-Code: C188814 Definition: A target study population on which an analysis is performed. These may be represented by the entire study population, a subgroup defined by a particular characteristic measured at baseline, or a principal stratum defined by the occurrence (or non-occurrence, depending on context) of a specific intercurrent event. (ICH E9 R1 Addendum) Preferred Term: Analysis Population

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**text** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**label** | **str** |  | 
**subset_of** | **List[str]** |  | [optional] 
**notes** | **List[str]** |  | [optional] 
**instance_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.analysis_population import AnalysisPopulation

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisPopulation from a JSON string
analysis_population_instance = AnalysisPopulation.from_json(json)
# print the JSON string representation of the object
print AnalysisPopulation.to_json()

# convert the object into a dict
analysis_population_dict = analysis_population_instance.to_dict()
# create an instance of AnalysisPopulation from a dict
analysis_population_from_dict = AnalysisPopulation.from_dict(analysis_population_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


