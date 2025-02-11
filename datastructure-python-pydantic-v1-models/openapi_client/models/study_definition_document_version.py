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

class StudyDefinitionDocumentVersion(BaseModel):
    """
    NCI C-Code: CNEW Definition: A representation of a particular edition or snapshot of the study definition document as it exists at a particular point in time. Preferred Term: Study Definition Document Version  # noqa: E501
    """
    id: StrictStr = Field(...)
    version: StrictStr = Field(...)
    status: StrictStr = Field(...)
    notes: Optional[conlist(StrictStr)] = None
    date_values: Optional[conlist(StrictStr)] = Field(default=None, alias="dateValues")
    contents: Optional[conlist(StrictStr)] = None
    children: Optional[conlist(StrictStr)] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "version", "status", "notes", "dateValues", "contents", "children", "instanceType"]

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
    def from_json(cls, json_str: str) -> StudyDefinitionDocumentVersion:
        """Create an instance of StudyDefinitionDocumentVersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyDefinitionDocumentVersion:
        """Create an instance of StudyDefinitionDocumentVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyDefinitionDocumentVersion.parse_obj(obj)

        _obj = StudyDefinitionDocumentVersion.parse_obj({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "status": obj.get("status"),
            "notes": obj.get("notes"),
            "date_values": obj.get("dateValues"),
            "contents": obj.get("contents"),
            "children": obj.get("children"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


