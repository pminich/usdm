# coding: utf-8

"""
    DDF USDM API

    A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.

    The version of the OpenAPI document: 3.10.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.intercurrent_event_input import IntercurrentEventInput

class EstimandInput(BaseModel):
    """
    EstimandInput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    population_summary: StrictStr = Field(default=..., alias="populationSummary")
    analysis_population_id: StrictStr = Field(default=..., alias="analysisPopulationId")
    intervention_ids: conlist(StrictStr) = Field(default=..., alias="interventionIds")
    variable_of_interest_id: StrictStr = Field(default=..., alias="variableOfInterestId")
    intercurrent_events: conlist(IntercurrentEventInput) = Field(default=..., alias="intercurrentEvents")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "populationSummary", "analysisPopulationId", "interventionIds", "variableOfInterestId", "intercurrentEvents", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Estimand',):
            raise ValueError("must be one of enum values ('Estimand')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EstimandInput:
        """Create an instance of EstimandInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in intercurrent_events (list)
        _items = []
        if self.intercurrent_events:
            for _item in self.intercurrent_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['intercurrentEvents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EstimandInput:
        """Create an instance of EstimandInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EstimandInput.parse_obj(obj)

        _obj = EstimandInput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "population_summary": obj.get("populationSummary"),
            "analysis_population_id": obj.get("analysisPopulationId"),
            "intervention_ids": obj.get("interventionIds"),
            "variable_of_interest_id": obj.get("variableOfInterestId"),
            "intercurrent_events": [IntercurrentEventInput.from_dict(_item) for _item in obj.get("intercurrentEvents")] if obj.get("intercurrentEvents") is not None else None,
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


