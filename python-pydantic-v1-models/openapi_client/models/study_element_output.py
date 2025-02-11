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
from openapi_client.models.transition_rule import TransitionRule

class StudyElementOutput(BaseModel):
    """
    StudyElementOutput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    name: constr(strict=True, min_length=1) = Field(...)
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    transition_start_rule: Optional[TransitionRule] = Field(default=None, alias="transitionStartRule")
    transition_end_rule: Optional[TransitionRule] = Field(default=None, alias="transitionEndRule")
    study_intervention_ids: Optional[conlist(StrictStr)] = Field(default=None, alias="studyInterventionIds")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "name", "label", "description", "transitionStartRule", "transitionEndRule", "studyInterventionIds", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('StudyElement',):
            raise ValueError("must be one of enum values ('StudyElement')")
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
    def from_json(cls, json_str: str) -> StudyElementOutput:
        """Create an instance of StudyElementOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> StudyElementOutput:
        """Create an instance of StudyElementOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyElementOutput.parse_obj(obj)

        _obj = StudyElementOutput.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "transition_start_rule": TransitionRule.from_dict(obj.get("transitionStartRule")) if obj.get("transitionStartRule") is not None else None,
            "transition_end_rule": TransitionRule.from_dict(obj.get("transitionEndRule")) if obj.get("transitionEndRule") is not None else None,
            "study_intervention_ids": obj.get("studyInterventionIds"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


