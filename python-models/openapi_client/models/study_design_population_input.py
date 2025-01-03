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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.code import Code
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.range_input import RangeInput
from openapi_client.models.study_cohort_input import StudyCohortInput
from typing import Optional, Set
from typing_extensions import Self

class StudyDesignPopulationInput(BaseModel):
    """
    StudyDesignPopulationInput
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    name: Annotated[str, Field(min_length=1, strict=True)]
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    includes_healthy_subjects: StrictBool = Field(alias="includesHealthySubjects")
    planned_enrollment_number: Optional[RangeInput] = Field(default=None, alias="plannedEnrollmentNumber")
    planned_completion_number: Optional[RangeInput] = Field(default=None, alias="plannedCompletionNumber")
    planned_sex: Optional[Annotated[List[Code], Field(max_length=2)]] = Field(default=None, alias="plannedSex")
    criterion_ids: Optional[List[StrictStr]] = Field(default=None, alias="criterionIds")
    planned_age: Optional[RangeInput] = Field(default=None, alias="plannedAge")
    notes: Optional[List[CommentAnnotation]] = None
    instance_type: StrictStr = Field(alias="instanceType")
    cohorts: Optional[List[StudyCohortInput]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "label", "description", "includesHealthySubjects", "plannedEnrollmentNumber", "plannedCompletionNumber", "plannedSex", "criterionIds", "plannedAge", "notes", "instanceType", "cohorts"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['StudyDesignPopulation']):
            raise ValueError("must be one of enum values ('StudyDesignPopulation')")
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
        """Create an instance of StudyDesignPopulationInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of planned_enrollment_number
        if self.planned_enrollment_number:
            _dict['plannedEnrollmentNumber'] = self.planned_enrollment_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of planned_completion_number
        if self.planned_completion_number:
            _dict['plannedCompletionNumber'] = self.planned_completion_number.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in planned_sex (list)
        _items = []
        if self.planned_sex:
            for _item_planned_sex in self.planned_sex:
                if _item_planned_sex:
                    _items.append(_item_planned_sex.to_dict())
            _dict['plannedSex'] = _items
        # override the default output from pydantic by calling `to_dict()` of planned_age
        if self.planned_age:
            _dict['plannedAge'] = self.planned_age.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cohorts (list)
        _items = []
        if self.cohorts:
            for _item_cohorts in self.cohorts:
                if _item_cohorts:
                    _items.append(_item_cohorts.to_dict())
            _dict['cohorts'] = _items
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if planned_enrollment_number (nullable) is None
        # and model_fields_set contains the field
        if self.planned_enrollment_number is None and "planned_enrollment_number" in self.model_fields_set:
            _dict['plannedEnrollmentNumber'] = None

        # set to None if planned_completion_number (nullable) is None
        # and model_fields_set contains the field
        if self.planned_completion_number is None and "planned_completion_number" in self.model_fields_set:
            _dict['plannedCompletionNumber'] = None

        # set to None if planned_age (nullable) is None
        # and model_fields_set contains the field
        if self.planned_age is None and "planned_age" in self.model_fields_set:
            _dict['plannedAge'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudyDesignPopulationInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "includesHealthySubjects": obj.get("includesHealthySubjects"),
            "plannedEnrollmentNumber": RangeInput.from_dict(obj["plannedEnrollmentNumber"]) if obj.get("plannedEnrollmentNumber") is not None else None,
            "plannedCompletionNumber": RangeInput.from_dict(obj["plannedCompletionNumber"]) if obj.get("plannedCompletionNumber") is not None else None,
            "plannedSex": [Code.from_dict(_item) for _item in obj["plannedSex"]] if obj.get("plannedSex") is not None else None,
            "criterionIds": obj.get("criterionIds"),
            "plannedAge": RangeInput.from_dict(obj["plannedAge"]) if obj.get("plannedAge") is not None else None,
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "instanceType": obj.get("instanceType"),
            "cohorts": [StudyCohortInput.from_dict(_item) for _item in obj["cohorts"]] if obj.get("cohorts") is not None else None
        })
        return _obj


