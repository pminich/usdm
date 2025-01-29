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

class StudyDefinitionDocument(BaseModel):
    """
    NCI C-Code: CNEW Definition: Any physical or electronic document that is related to defining a study or part of a study. Preferred Term: Study Definition Document  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    description: StrictStr = Field(...)
    label: StrictStr = Field(...)
    template_name: StrictStr = Field(default=..., alias="templateName")
    language: StrictStr = Field(...)
    type: StrictStr = Field(...)
    notes: Optional[conlist(StrictStr)] = None
    versions: Optional[conlist(StrictStr)] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "name", "description", "label", "templateName", "language", "type", "notes", "versions", "instanceType"]

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
    def from_json(cls, json_str: str) -> StudyDefinitionDocument:
        """Create an instance of StudyDefinitionDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyDefinitionDocument:
        """Create an instance of StudyDefinitionDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyDefinitionDocument.parse_obj(obj)

        _obj = StudyDefinitionDocument.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "label": obj.get("label"),
            "template_name": obj.get("templateName"),
            "language": obj.get("language"),
            "type": obj.get("type"),
            "notes": obj.get("notes"),
            "versions": obj.get("versions"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


