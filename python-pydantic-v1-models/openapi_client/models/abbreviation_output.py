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

class AbbreviationOutput(BaseModel):
    """
    AbbreviationOutput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    abbreviated_text: constr(strict=True, min_length=1) = Field(default=..., alias="abbreviatedText")
    expanded_text: constr(strict=True, min_length=1) = Field(default=..., alias="expandedText")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "abbreviatedText", "expandedText", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Abbreviation',):
            raise ValueError("must be one of enum values ('Abbreviation')")
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
    def from_json(cls, json_str: str) -> AbbreviationOutput:
        """Create an instance of AbbreviationOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AbbreviationOutput:
        """Create an instance of AbbreviationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AbbreviationOutput.parse_obj(obj)

        _obj = AbbreviationOutput.parse_obj({
            "id": obj.get("id"),
            "abbreviated_text": obj.get("abbreviatedText"),
            "expanded_text": obj.get("expandedText"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


