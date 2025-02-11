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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.geographic_scope_output import GeographicScopeOutput
from openapi_client.models.governance_date_output import GovernanceDateOutput
from openapi_client.models.study_amendment_impact_output import StudyAmendmentImpactOutput
from openapi_client.models.study_amendment_reason import StudyAmendmentReason
from openapi_client.models.study_change import StudyChange
from openapi_client.models.subject_enrollment_output import SubjectEnrollmentOutput
from typing import Optional, Set
from typing_extensions import Self

class StudyAmendmentOutput(BaseModel):
    """
    StudyAmendmentOutput
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    number: StrictStr
    summary: StrictStr
    primary_reason: StudyAmendmentReason = Field(alias="primaryReason")
    secondary_reasons: Optional[List[StudyAmendmentReason]] = Field(default=None, alias="secondaryReasons")
    changes: List[StudyChange]
    impacts: Optional[List[StudyAmendmentImpactOutput]] = None
    geographic_scopes: List[GeographicScopeOutput] = Field(alias="geographicScopes")
    enrollments: Optional[List[SubjectEnrollmentOutput]] = None
    date_values: Optional[List[GovernanceDateOutput]] = Field(default=None, alias="dateValues")
    previous_id: Optional[StrictStr] = Field(default=None, alias="previousId")
    notes: Optional[List[CommentAnnotation]] = None
    instance_type: StrictStr = Field(alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "number", "summary", "primaryReason", "secondaryReasons", "changes", "impacts", "geographicScopes", "enrollments", "dateValues", "previousId", "notes", "instanceType"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['StudyAmendment']):
            raise ValueError("must be one of enum values ('StudyAmendment')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StudyAmendmentOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of primary_reason
        if self.primary_reason:
            _dict['primaryReason'] = self.primary_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_reasons (list)
        _items = []
        if self.secondary_reasons:
            for _item_secondary_reasons in self.secondary_reasons:
                if _item_secondary_reasons:
                    _items.append(_item_secondary_reasons.to_dict())
            _dict['secondaryReasons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item_changes in self.changes:
                if _item_changes:
                    _items.append(_item_changes.to_dict())
            _dict['changes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in impacts (list)
        _items = []
        if self.impacts:
            for _item_impacts in self.impacts:
                if _item_impacts:
                    _items.append(_item_impacts.to_dict())
            _dict['impacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in geographic_scopes (list)
        _items = []
        if self.geographic_scopes:
            for _item_geographic_scopes in self.geographic_scopes:
                if _item_geographic_scopes:
                    _items.append(_item_geographic_scopes.to_dict())
            _dict['geographicScopes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in enrollments (list)
        _items = []
        if self.enrollments:
            for _item_enrollments in self.enrollments:
                if _item_enrollments:
                    _items.append(_item_enrollments.to_dict())
            _dict['enrollments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in date_values (list)
        _items = []
        if self.date_values:
            for _item_date_values in self.date_values:
                if _item_date_values:
                    _items.append(_item_date_values.to_dict())
            _dict['dateValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        # set to None if previous_id (nullable) is None
        # and model_fields_set contains the field
        if self.previous_id is None and "previous_id" in self.model_fields_set:
            _dict['previousId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudyAmendmentOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "number": obj.get("number"),
            "summary": obj.get("summary"),
            "primaryReason": StudyAmendmentReason.from_dict(obj["primaryReason"]) if obj.get("primaryReason") is not None else None,
            "secondaryReasons": [StudyAmendmentReason.from_dict(_item) for _item in obj["secondaryReasons"]] if obj.get("secondaryReasons") is not None else None,
            "changes": [StudyChange.from_dict(_item) for _item in obj["changes"]] if obj.get("changes") is not None else None,
            "impacts": [StudyAmendmentImpactOutput.from_dict(_item) for _item in obj["impacts"]] if obj.get("impacts") is not None else None,
            "geographicScopes": [GeographicScopeOutput.from_dict(_item) for _item in obj["geographicScopes"]] if obj.get("geographicScopes") is not None else None,
            "enrollments": [SubjectEnrollmentOutput.from_dict(_item) for _item in obj["enrollments"]] if obj.get("enrollments") is not None else None,
            "dateValues": [GovernanceDateOutput.from_dict(_item) for _item in obj["dateValues"]] if obj.get("dateValues") is not None else None,
            "previousId": obj.get("previousId"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "instanceType": obj.get("instanceType")
        })
        return _obj


