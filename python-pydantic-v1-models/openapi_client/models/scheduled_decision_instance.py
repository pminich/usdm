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
from openapi_client.models.condition_assignment import ConditionAssignment

class ScheduledDecisionInstance(BaseModel):
    """
    ScheduledDecisionInstance
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    default_condition_id: Optional[StrictStr] = Field(default=None, alias="defaultConditionId")
    epoch_id: Optional[StrictStr] = Field(default=None, alias="epochId")
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    condition_assignments: conlist(ConditionAssignment) = Field(default=..., alias="conditionAssignments")
    __properties = ["id", "name", "label", "description", "defaultConditionId", "epochId", "instanceType", "conditionAssignments"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ScheduledDecisionInstance',):
            raise ValueError("must be one of enum values ('ScheduledDecisionInstance')")
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
    def from_json(cls, json_str: str) -> ScheduledDecisionInstance:
        """Create an instance of ScheduledDecisionInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in condition_assignments (list)
        _items = []
        if self.condition_assignments:
            for _item in self.condition_assignments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditionAssignments'] = _items
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if default_condition_id (nullable) is None
        # and __fields_set__ contains the field
        if self.default_condition_id is None and "default_condition_id" in self.__fields_set__:
            _dict['defaultConditionId'] = None

        # set to None if epoch_id (nullable) is None
        # and __fields_set__ contains the field
        if self.epoch_id is None and "epoch_id" in self.__fields_set__:
            _dict['epochId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScheduledDecisionInstance:
        """Create an instance of ScheduledDecisionInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScheduledDecisionInstance.parse_obj(obj)

        _obj = ScheduledDecisionInstance.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "default_condition_id": obj.get("defaultConditionId"),
            "epoch_id": obj.get("epochId"),
            "instance_type": obj.get("instanceType"),
            "condition_assignments": [ConditionAssignment.from_dict(_item) for _item in obj.get("conditionAssignments")] if obj.get("conditionAssignments") is not None else None
        })
        return _obj


