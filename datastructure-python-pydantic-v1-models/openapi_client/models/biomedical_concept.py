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

class BiomedicalConcept(BaseModel):
    """
    NCI C-Code: C201345 Definition: A unit of biomedical knowledge created from a unique combination of characteristics that include implementation details like variables and terminologies, used as building blocks for standardized, hierarchically structured clinical research information. Preferred Term: Biomedical Concept  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    label: StrictStr = Field(...)
    synonyms: StrictStr = Field(...)
    reference: StrictStr = Field(...)
    code: StrictStr = Field(...)
    notes: Optional[conlist(StrictStr)] = None
    properties: Optional[conlist(StrictStr)] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "name", "label", "synonyms", "reference", "code", "notes", "properties", "instanceType"]

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
    def from_json(cls, json_str: str) -> BiomedicalConcept:
        """Create an instance of BiomedicalConcept from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BiomedicalConcept:
        """Create an instance of BiomedicalConcept from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BiomedicalConcept.parse_obj(obj)

        _obj = BiomedicalConcept.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "synonyms": obj.get("synonyms"),
            "reference": obj.get("reference"),
            "code": obj.get("code"),
            "notes": obj.get("notes"),
            "properties": obj.get("properties"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


