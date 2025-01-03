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
from openapi_client.models.administration_duration_output import AdministrationDurationOutput
from openapi_client.models.alias_code import AliasCode
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.quantity_output import QuantityOutput
from typing import Optional, Set
from typing_extensions import Self

class AdministrationOutput(BaseModel):
    """
    AdministrationOutput
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    name: Annotated[str, Field(min_length=1, strict=True)]
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    duration: AdministrationDurationOutput
    dose: Optional[QuantityOutput]
    route: Optional[AliasCode]
    frequency: Optional[AliasCode]
    administrable_product_id: Optional[StrictStr] = Field(default=None, alias="administrableProductId")
    medical_device_id: Optional[StrictStr] = Field(default=None, alias="medicalDeviceId")
    notes: Optional[List[CommentAnnotation]] = None
    instance_type: StrictStr = Field(alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "name", "label", "description", "duration", "dose", "route", "frequency", "administrableProductId", "medicalDeviceId", "notes", "instanceType"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Administration']):
            raise ValueError("must be one of enum values ('Administration')")
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
        """Create an instance of AdministrationOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dose
        if self.dose:
            _dict['dose'] = self.dose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of route
        if self.route:
            _dict['route'] = self.route.to_dict()
        # override the default output from pydantic by calling `to_dict()` of frequency
        if self.frequency:
            _dict['frequency'] = self.frequency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if dose (nullable) is None
        # and model_fields_set contains the field
        if self.dose is None and "dose" in self.model_fields_set:
            _dict['dose'] = None

        # set to None if route (nullable) is None
        # and model_fields_set contains the field
        if self.route is None and "route" in self.model_fields_set:
            _dict['route'] = None

        # set to None if frequency (nullable) is None
        # and model_fields_set contains the field
        if self.frequency is None and "frequency" in self.model_fields_set:
            _dict['frequency'] = None

        # set to None if administrable_product_id (nullable) is None
        # and model_fields_set contains the field
        if self.administrable_product_id is None and "administrable_product_id" in self.model_fields_set:
            _dict['administrableProductId'] = None

        # set to None if medical_device_id (nullable) is None
        # and model_fields_set contains the field
        if self.medical_device_id is None and "medical_device_id" in self.model_fields_set:
            _dict['medicalDeviceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdministrationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "duration": AdministrationDurationOutput.from_dict(obj["duration"]) if obj.get("duration") is not None else None,
            "dose": QuantityOutput.from_dict(obj["dose"]) if obj.get("dose") is not None else None,
            "route": AliasCode.from_dict(obj["route"]) if obj.get("route") is not None else None,
            "frequency": AliasCode.from_dict(obj["frequency"]) if obj.get("frequency") is not None else None,
            "administrableProductId": obj.get("administrableProductId"),
            "medicalDeviceId": obj.get("medicalDeviceId"),
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "instanceType": obj.get("instanceType")
        })
        return _obj


