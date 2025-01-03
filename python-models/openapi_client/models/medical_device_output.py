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
from openapi_client.models.code import Code
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.medical_device_identifier import MedicalDeviceIdentifier
from typing import Optional, Set
from typing_extensions import Self

class MedicalDeviceOutput(BaseModel):
    """
    MedicalDeviceOutput
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    name: Annotated[str, Field(min_length=1, strict=True)]
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    hardware_version: Optional[StrictStr] = Field(default=None, alias="hardwareVersion")
    software_version: Optional[StrictStr] = Field(default=None, alias="softwareVersion")
    embedded_product_id: Optional[StrictStr] = Field(default=None, alias="embeddedProductId")
    sourcing: Optional[Code] = None
    identifiers: Optional[List[MedicalDeviceIdentifier]] = None
    notes: Optional[List[CommentAnnotation]] = None
    instance_type: StrictStr = Field(alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "name", "label", "description", "hardwareVersion", "softwareVersion", "embeddedProductId", "sourcing", "identifiers", "notes", "instanceType"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MedicalDevice']):
            raise ValueError("must be one of enum values ('MedicalDevice')")
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
        """Create an instance of MedicalDeviceOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sourcing
        if self.sourcing:
            _dict['sourcing'] = self.sourcing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item_identifiers in self.identifiers:
                if _item_identifiers:
                    _items.append(_item_identifiers.to_dict())
            _dict['identifiers'] = _items
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

        # set to None if hardware_version (nullable) is None
        # and model_fields_set contains the field
        if self.hardware_version is None and "hardware_version" in self.model_fields_set:
            _dict['hardwareVersion'] = None

        # set to None if software_version (nullable) is None
        # and model_fields_set contains the field
        if self.software_version is None and "software_version" in self.model_fields_set:
            _dict['softwareVersion'] = None

        # set to None if embedded_product_id (nullable) is None
        # and model_fields_set contains the field
        if self.embedded_product_id is None and "embedded_product_id" in self.model_fields_set:
            _dict['embeddedProductId'] = None

        # set to None if sourcing (nullable) is None
        # and model_fields_set contains the field
        if self.sourcing is None and "sourcing" in self.model_fields_set:
            _dict['sourcing'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MedicalDeviceOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "hardwareVersion": obj.get("hardwareVersion"),
            "softwareVersion": obj.get("softwareVersion"),
            "embeddedProductId": obj.get("embeddedProductId"),
            "sourcing": Code.from_dict(obj["sourcing"]) if obj.get("sourcing") is not None else None,
            "identifiers": [MedicalDeviceIdentifier.from_dict(_item) for _item in obj["identifiers"]] if obj.get("identifiers") is not None else None,
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "instanceType": obj.get("instanceType")
        })
        return _obj

