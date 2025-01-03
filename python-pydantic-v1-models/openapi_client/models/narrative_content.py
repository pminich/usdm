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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator

class NarrativeContent(BaseModel):
    """
    NarrativeContent
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    section_number: Optional[StrictStr] = Field(default=None, alias="sectionNumber")
    section_title: Optional[StrictStr] = Field(default=None, alias="sectionTitle")
    display_section_number: StrictBool = Field(default=..., alias="displaySectionNumber")
    display_section_title: StrictBool = Field(default=..., alias="displaySectionTitle")
    child_ids: Optional[conlist(StrictStr)] = Field(default=None, alias="childIds")
    previous_id: Optional[StrictStr] = Field(default=None, alias="previousId")
    next_id: Optional[StrictStr] = Field(default=None, alias="nextId")
    content_item_id: Optional[StrictStr] = Field(default=None, alias="contentItemId")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "sectionNumber", "sectionTitle", "displaySectionNumber", "displaySectionTitle", "childIds", "previousId", "nextId", "contentItemId", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('NarrativeContent',):
            raise ValueError("must be one of enum values ('NarrativeContent')")
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
    def from_json(cls, json_str: str) -> NarrativeContent:
        """Create an instance of NarrativeContent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if section_number (nullable) is None
        # and __fields_set__ contains the field
        if self.section_number is None and "section_number" in self.__fields_set__:
            _dict['sectionNumber'] = None

        # set to None if section_title (nullable) is None
        # and __fields_set__ contains the field
        if self.section_title is None and "section_title" in self.__fields_set__:
            _dict['sectionTitle'] = None

        # set to None if previous_id (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_id is None and "previous_id" in self.__fields_set__:
            _dict['previousId'] = None

        # set to None if next_id (nullable) is None
        # and __fields_set__ contains the field
        if self.next_id is None and "next_id" in self.__fields_set__:
            _dict['nextId'] = None

        # set to None if content_item_id (nullable) is None
        # and __fields_set__ contains the field
        if self.content_item_id is None and "content_item_id" in self.__fields_set__:
            _dict['contentItemId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NarrativeContent:
        """Create an instance of NarrativeContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NarrativeContent.parse_obj(obj)

        _obj = NarrativeContent.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "section_number": obj.get("sectionNumber"),
            "section_title": obj.get("sectionTitle"),
            "display_section_number": obj.get("displaySectionNumber"),
            "display_section_title": obj.get("displaySectionTitle"),
            "child_ids": obj.get("childIds"),
            "previous_id": obj.get("previousId"),
            "next_id": obj.get("nextId"),
            "content_item_id": obj.get("contentItemId"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


