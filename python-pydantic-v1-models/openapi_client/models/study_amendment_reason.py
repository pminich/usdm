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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from openapi_client.models.code import Code

class StudyAmendmentReason(BaseModel):
    """
    StudyAmendmentReason
    """
    id: constr(strict=True, min_length=1) = Field(...)
    code: Code = Field(...)
    other_reason: Optional[StrictStr] = Field(default=None, alias="otherReason")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "code", "otherReason", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('StudyAmendmentReason',):
            raise ValueError("must be one of enum values ('StudyAmendmentReason')")
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
    def from_json(cls, json_str: str) -> StudyAmendmentReason:
        """Create an instance of StudyAmendmentReason from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # set to None if other_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.other_reason is None and "other_reason" in self.__fields_set__:
            _dict['otherReason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyAmendmentReason:
        """Create an instance of StudyAmendmentReason from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyAmendmentReason.parse_obj(obj)

        _obj = StudyAmendmentReason.parse_obj({
            "id": obj.get("id"),
            "code": Code.from_dict(obj.get("code")) if obj.get("code") is not None else None,
            "other_reason": obj.get("otherReason"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


