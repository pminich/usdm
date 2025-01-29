# coding: utf-8

"""
    USDM to OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class Objective(BaseModel):
    """
    NCI C-Code: C142450 Definition: The reason for performing a study in terms of the scientific questions to be answered by the analysis of data collected during the study. Preferred Term: Study Objective  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    description: StrictStr = Field(...)
    label: StrictStr = Field(...)
    text: StrictStr = Field(...)
    notes: Optional[conlist(StrictStr)] = None
    dictionary: Optional[StrictStr] = None
    level: StrictStr = Field(...)
    endpoints: Optional[conlist(StrictStr)] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "name", "description", "label", "text", "notes", "dictionary", "level", "endpoints", "instanceType"]

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
    def from_json(cls, json_str: str) -> Objective:
        """Create an instance of Objective from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Objective:
        """Create an instance of Objective from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Objective.parse_obj(obj)

        _obj = Objective.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "label": obj.get("label"),
            "text": obj.get("text"),
            "notes": obj.get("notes"),
            "dictionary": obj.get("dictionary"),
            "level": obj.get("level"),
            "endpoints": obj.get("endpoints"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


