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
from openapi_client.models.geographic_scope_output import GeographicScopeOutput
from openapi_client.models.governance_date_output import GovernanceDateOutput
from openapi_client.models.study_amendment_impact_output import StudyAmendmentImpactOutput
from openapi_client.models.study_amendment_reason import StudyAmendmentReason
from openapi_client.models.study_change import StudyChange
from openapi_client.models.subject_enrollment_output import SubjectEnrollmentOutput

class StudyAmendmentOutput(BaseModel):
    """
    StudyAmendmentOutput
    """
    id: constr(strict=True, min_length=1) = Field(...)
    number: StrictStr = Field(...)
    summary: StrictStr = Field(...)
    primary_reason: StudyAmendmentReason = Field(default=..., alias="primaryReason")
    secondary_reasons: Optional[conlist(StudyAmendmentReason)] = Field(default=None, alias="secondaryReasons")
    changes: conlist(StudyChange) = Field(...)
    impacts: Optional[conlist(StudyAmendmentImpactOutput)] = None
    geographic_scopes: conlist(GeographicScopeOutput) = Field(default=..., alias="geographicScopes")
    enrollments: Optional[conlist(SubjectEnrollmentOutput)] = None
    date_values: Optional[conlist(GovernanceDateOutput)] = Field(default=None, alias="dateValues")
    previous_id: Optional[StrictStr] = Field(default=None, alias="previousId")
    notes: Optional[conlist(CommentAnnotation)] = None
    instance_type: StrictStr = Field(default=..., alias="instanceType")
    __properties = ["id", "number", "summary", "primaryReason", "secondaryReasons", "changes", "impacts", "geographicScopes", "enrollments", "dateValues", "previousId", "notes", "instanceType"]

    @validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('StudyAmendment',):
            raise ValueError("must be one of enum values ('StudyAmendment')")
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
    def from_json(cls, json_str: str) -> StudyAmendmentOutput:
        """Create an instance of StudyAmendmentOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of primary_reason
        if self.primary_reason:
            _dict['primaryReason'] = self.primary_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_reasons (list)
        _items = []
        if self.secondary_reasons:
            for _item in self.secondary_reasons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secondaryReasons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item in self.changes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['changes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in impacts (list)
        _items = []
        if self.impacts:
            for _item in self.impacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['impacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in geographic_scopes (list)
        _items = []
        if self.geographic_scopes:
            for _item in self.geographic_scopes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['geographicScopes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in enrollments (list)
        _items = []
        if self.enrollments:
            for _item in self.enrollments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['enrollments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in date_values (list)
        _items = []
        if self.date_values:
            for _item in self.date_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dateValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # set to None if previous_id (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_id is None and "previous_id" in self.__fields_set__:
            _dict['previousId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyAmendmentOutput:
        """Create an instance of StudyAmendmentOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyAmendmentOutput.parse_obj(obj)

        _obj = StudyAmendmentOutput.parse_obj({
            "id": obj.get("id"),
            "number": obj.get("number"),
            "summary": obj.get("summary"),
            "primary_reason": StudyAmendmentReason.from_dict(obj.get("primaryReason")) if obj.get("primaryReason") is not None else None,
            "secondary_reasons": [StudyAmendmentReason.from_dict(_item) for _item in obj.get("secondaryReasons")] if obj.get("secondaryReasons") is not None else None,
            "changes": [StudyChange.from_dict(_item) for _item in obj.get("changes")] if obj.get("changes") is not None else None,
            "impacts": [StudyAmendmentImpactOutput.from_dict(_item) for _item in obj.get("impacts")] if obj.get("impacts") is not None else None,
            "geographic_scopes": [GeographicScopeOutput.from_dict(_item) for _item in obj.get("geographicScopes")] if obj.get("geographicScopes") is not None else None,
            "enrollments": [SubjectEnrollmentOutput.from_dict(_item) for _item in obj.get("enrollments")] if obj.get("enrollments") is not None else None,
            "date_values": [GovernanceDateOutput.from_dict(_item) for _item in obj.get("dateValues")] if obj.get("dateValues") is not None else None,
            "previous_id": obj.get("previousId"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None,
            "instance_type": obj.get("instanceType")
        })
        return _obj


