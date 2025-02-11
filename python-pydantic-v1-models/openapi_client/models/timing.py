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

class Timing(BaseModel):
    """
    Timing
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    type: Code = Field(...)
    value: StrictStr = Field(...)
    value_label: StrictStr = Field(default=..., alias="valueLabel")
    relative_to_from: Code = Field(default=..., alias="relativeToFrom")
    relative_from_scheduled_instance_id: StrictStr = Field(default=..., alias="relativeFromScheduledInstanceId")
    relative_to_scheduled_instance_id: Optional[StrictStr] = Field(default=None, alias="relativeToScheduledInstanceId")
    window_lower: Optional[StrictStr] = Field(default=None, alias="windowLower")
    window_upper: Optional[StrictStr] = Field(default=None, alias="windowUpper")
    window_label: Optional[StrictStr] = Field(default=None, alias="windowLabel")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "type", "value", "valueLabel", "relativeToFrom", "relativeFromScheduledInstanceId", "relativeToScheduledInstanceId", "windowLower", "windowUpper", "windowLabel", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Timing',):
            raise ValueError("must be one of enum values ('Timing')")
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
    def from_json(cls, json_str: str) -> Timing:
        """Create an instance of Timing from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relative_to_from
        if self.relative_to_from:
            _dict['relativeToFrom'] = self.relative_to_from.to_dict()
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if relative_to_scheduled_instance_id (nullable) is None
        # and __fields_set__ contains the field
        if self.relative_to_scheduled_instance_id is None and "relative_to_scheduled_instance_id" in self.__fields_set__:
            _dict['relativeToScheduledInstanceId'] = None

        # set to None if window_lower (nullable) is None
        # and __fields_set__ contains the field
        if self.window_lower is None and "window_lower" in self.__fields_set__:
            _dict['windowLower'] = None

        # set to None if window_upper (nullable) is None
        # and __fields_set__ contains the field
        if self.window_upper is None and "window_upper" in self.__fields_set__:
            _dict['windowUpper'] = None

        # set to None if window_label (nullable) is None
        # and __fields_set__ contains the field
        if self.window_label is None and "window_label" in self.__fields_set__:
            _dict['windowLabel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Timing:
        """Create an instance of Timing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Timing.parse_obj(obj)

        _obj = Timing.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "type": Code.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "value": obj.get("value"),
            "value_label": obj.get("valueLabel"),
            "relative_to_from": Code.from_dict(obj.get("relativeToFrom")) if obj.get("relativeToFrom") is not None else None,
            "relative_from_scheduled_instance_id": obj.get("relativeFromScheduledInstanceId"),
            "relative_to_scheduled_instance_id": obj.get("relativeToScheduledInstanceId"),
            "window_lower": obj.get("windowLower"),
            "window_upper": obj.get("windowUpper"),
            "window_label": obj.get("windowLabel"),
            "instance_type": obj.get("instanceType")
        })
        return _obj


