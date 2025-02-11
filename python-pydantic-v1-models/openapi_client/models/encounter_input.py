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
from openapi_client.models.code import Code
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.transition_rule import TransitionRule

class EncounterInput(BaseModel):
    """
    EncounterInput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    type: Code = Field(...)
    previous_id: Optional[StrictStr] = Field(default=None, alias="previousId")
    next_id: Optional[StrictStr] = Field(default=None, alias="nextId")
    scheduled_at_id: Optional[StrictStr] = Field(default=None, alias="scheduledAtId")
    environmental_settings: Optional[conlist(Code)] = Field(default=None, alias="environmentalSettings")
    contact_modes: Optional[conlist(Code)] = Field(default=None, alias="contactModes")
    transition_start_rule: Optional[TransitionRule] = Field(default=None, alias="transitionStartRule")
    transition_end_rule: Optional[TransitionRule] = Field(default=None, alias="transitionEndRule")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "type", "previousId", "nextId", "scheduledAtId", "environmentalSettings", "contactModes", "transitionStartRule", "transitionEndRule", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Encounter',):
            raise ValueError("must be one of enum values ('Encounter')")
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
    def from_json(cls, json_str: str) -> EncounterInput:
        """Create an instance of EncounterInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in environmental_settings (list)
        _items = []
        if self.environmental_settings:
            for _item in self.environmental_settings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['environmentalSettings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in contact_modes (list)
        _items = []
        if self.contact_modes:
            for _item in self.contact_modes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contactModes'] = _items
        # override the default output from pydantic by calling `to_dict()` of transition_start_rule
        if self.transition_start_rule:
            _dict['transitionStartRule'] = self.transition_start_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transition_end_rule
        if self.transition_end_rule:
            _dict['transitionEndRule'] = self.transition_end_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if previous_id (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_id is None and "previous_id" in self.__fields_set__:
            _dict['previousId'] = None

        # set to None if next_id (nullable) is None
        # and __fields_set__ contains the field
        if self.next_id is None and "next_id" in self.__fields_set__:
            _dict['nextId'] = None

        # set to None if scheduled_at_id (nullable) is None
        # and __fields_set__ contains the field
        if self.scheduled_at_id is None and "scheduled_at_id" in self.__fields_set__:
            _dict['scheduledAtId'] = None

        # set to None if transition_start_rule (nullable) is None
        # and __fields_set__ contains the field
        if self.transition_start_rule is None and "transition_start_rule" in self.__fields_set__:
            _dict['transitionStartRule'] = None

        # set to None if transition_end_rule (nullable) is None
        # and __fields_set__ contains the field
        if self.transition_end_rule is None and "transition_end_rule" in self.__fields_set__:
            _dict['transitionEndRule'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EncounterInput:
        """Create an instance of EncounterInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EncounterInput.parse_obj(obj)

        _obj = EncounterInput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "type": Code.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "previous_id": obj.get("previousId"),
            "next_id": obj.get("nextId"),
            "scheduled_at_id": obj.get("scheduledAtId"),
            "environmental_settings": [Code.from_dict(_item) for _item in obj.get("environmentalSettings")] if obj.get("environmentalSettings") is not None else None,
            "contact_modes": [Code.from_dict(_item) for _item in obj.get("contactModes")] if obj.get("contactModes") is not None else None,
            "transition_start_rule": TransitionRule.from_dict(obj.get("transitionStartRule")) if obj.get("transitionStartRule") is not None else None,
            "transition_end_rule": TransitionRule.from_dict(obj.get("transitionEndRule")) if obj.get("transitionEndRule") is not None else None,
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


