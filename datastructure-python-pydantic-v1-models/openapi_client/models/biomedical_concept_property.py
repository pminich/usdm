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

class BiomedicalConceptProperty(BaseModel):
    """
    NCI C-Code: C202493 Definition: A characteristic from a set of characteristics used to define a biomedical concept. Preferred Term: Biomedical Concept Property  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    label: StrictStr = Field(...)
    is_required: StrictStr = Field(default=..., alias="isRequired")
    is_enabled: StrictStr = Field(default=..., alias="isEnabled")
    datatype: StrictStr = Field(...)
    code: StrictStr = Field(...)
    response_codes: Optional[conlist(StrictStr)] = Field(default=None, alias="responseCodes")
    notes: Optional[conlist(StrictStr)] = None
    instance_type: Optional[StrictStr] = Field(default=None, alias="instanceType")
    __properties = ["id", "name", "label", "isRequired", "isEnabled", "datatype", "code", "responseCodes", "notes", "instanceType"]

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
    def from_json(cls, json_str: str) -> BiomedicalConceptProperty:
        """Create an instance of BiomedicalConceptProperty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BiomedicalConceptProperty:
        """Create an instance of BiomedicalConceptProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BiomedicalConceptProperty.parse_obj(obj)

        _obj = BiomedicalConceptProperty.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "is_required": obj.get("isRequired"),
            "is_enabled": obj.get("isEnabled"),
            "datatype": obj.get("datatype"),
            "code": obj.get("code"),
            "response_codes": obj.get("responseCodes"),
            "notes": obj.get("notes"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


