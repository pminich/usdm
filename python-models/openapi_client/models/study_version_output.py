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
from openapi_client.models.abbreviation_output import AbbreviationOutput
from openapi_client.models.administrable_product_output import AdministrableProductOutput
from openapi_client.models.code import Code
from openapi_client.models.comment_annotation import CommentAnnotation
from openapi_client.models.eligibility_criterion_output import EligibilityCriterionOutput
from openapi_client.models.governance_date_output import GovernanceDateOutput
from openapi_client.models.medical_device_output import MedicalDeviceOutput
from openapi_client.models.narrative_content_item import NarrativeContentItem
from openapi_client.models.organization_output import OrganizationOutput
from openapi_client.models.product_organization_role import ProductOrganizationRole
from openapi_client.models.reference_identifier import ReferenceIdentifier
from openapi_client.models.search_study_design_v3_study_designs_get200_response_inner import SearchStudyDesignV3StudyDesignsGet200ResponseInner
from openapi_client.models.study_amendment_output import StudyAmendmentOutput
from openapi_client.models.study_identifier import StudyIdentifier
from openapi_client.models.study_role import StudyRole
from openapi_client.models.study_title import StudyTitle
from typing import Optional, Set
from typing_extensions import Self

class StudyVersionOutput(BaseModel):
    """
    StudyVersionOutput
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True)]
    version_identifier: StrictStr = Field(alias="versionIdentifier")
    rationale: StrictStr
    document_version_ids: Optional[List[StrictStr]] = Field(default=None, alias="documentVersionIds")
    date_values: Optional[List[GovernanceDateOutput]] = Field(default=None, alias="dateValues")
    amendments: Optional[List[StudyAmendmentOutput]] = None
    business_therapeutic_areas: Optional[List[Code]] = Field(default=None, alias="businessTherapeuticAreas")
    study_identifiers: List[StudyIdentifier] = Field(alias="studyIdentifiers")
    reference_identifiers: Optional[List[ReferenceIdentifier]] = Field(default=None, alias="referenceIdentifiers")
    study_designs: Optional[List[SearchStudyDesignV3StudyDesignsGet200ResponseInner]] = Field(default=None, alias="studyDesigns")
    titles: List[StudyTitle]
    criteria: List[EligibilityCriterionOutput]
    narrative_content_items: Optional[List[NarrativeContentItem]] = Field(default=None, alias="narrativeContentItems")
    abbreviations: Optional[List[AbbreviationOutput]] = None
    roles: Optional[List[StudyRole]] = None
    organizations: Optional[List[OrganizationOutput]] = None
    administrable_products: Optional[List[AdministrableProductOutput]] = Field(default=None, alias="administrableProducts")
    medical_devices: Optional[List[MedicalDeviceOutput]] = Field(default=None, alias="medicalDevices")
    product_organization_roles: Optional[List[ProductOrganizationRole]] = Field(default=None, alias="productOrganizationRoles")
    notes: Optional[List[CommentAnnotation]] = None
    instance_type: StrictStr = Field(alias="instanceType")
    __properties: ClassVar[List[str]] = ["id", "versionIdentifier", "rationale", "documentVersionIds", "dateValues", "amendments", "businessTherapeuticAreas", "studyIdentifiers", "referenceIdentifiers", "studyDesigns", "titles", "criteria", "narrativeContentItems", "abbreviations", "roles", "organizations", "administrableProducts", "medicalDevices", "productOrganizationRoles", "notes", "instanceType"]

    @field_validator('instance_type')
    def instance_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['StudyVersion']):
            raise ValueError("must be one of enum values ('StudyVersion')")
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
        """Create an instance of StudyVersionOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in date_values (list)
        _items = []
        if self.date_values:
            for _item_date_values in self.date_values:
                if _item_date_values:
                    _items.append(_item_date_values.to_dict())
            _dict['dateValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in amendments (list)
        _items = []
        if self.amendments:
            for _item_amendments in self.amendments:
                if _item_amendments:
                    _items.append(_item_amendments.to_dict())
            _dict['amendments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in business_therapeutic_areas (list)
        _items = []
        if self.business_therapeutic_areas:
            for _item_business_therapeutic_areas in self.business_therapeutic_areas:
                if _item_business_therapeutic_areas:
                    _items.append(_item_business_therapeutic_areas.to_dict())
            _dict['businessTherapeuticAreas'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in study_identifiers (list)
        _items = []
        if self.study_identifiers:
            for _item_study_identifiers in self.study_identifiers:
                if _item_study_identifiers:
                    _items.append(_item_study_identifiers.to_dict())
            _dict['studyIdentifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reference_identifiers (list)
        _items = []
        if self.reference_identifiers:
            for _item_reference_identifiers in self.reference_identifiers:
                if _item_reference_identifiers:
                    _items.append(_item_reference_identifiers.to_dict())
            _dict['referenceIdentifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in study_designs (list)
        _items = []
        if self.study_designs:
            for _item_study_designs in self.study_designs:
                if _item_study_designs:
                    _items.append(_item_study_designs.to_dict())
            _dict['studyDesigns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in titles (list)
        _items = []
        if self.titles:
            for _item_titles in self.titles:
                if _item_titles:
                    _items.append(_item_titles.to_dict())
            _dict['titles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in criteria (list)
        _items = []
        if self.criteria:
            for _item_criteria in self.criteria:
                if _item_criteria:
                    _items.append(_item_criteria.to_dict())
            _dict['criteria'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in narrative_content_items (list)
        _items = []
        if self.narrative_content_items:
            for _item_narrative_content_items in self.narrative_content_items:
                if _item_narrative_content_items:
                    _items.append(_item_narrative_content_items.to_dict())
            _dict['narrativeContentItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in abbreviations (list)
        _items = []
        if self.abbreviations:
            for _item_abbreviations in self.abbreviations:
                if _item_abbreviations:
                    _items.append(_item_abbreviations.to_dict())
            _dict['abbreviations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item_roles in self.roles:
                if _item_roles:
                    _items.append(_item_roles.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in organizations (list)
        _items = []
        if self.organizations:
            for _item_organizations in self.organizations:
                if _item_organizations:
                    _items.append(_item_organizations.to_dict())
            _dict['organizations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in administrable_products (list)
        _items = []
        if self.administrable_products:
            for _item_administrable_products in self.administrable_products:
                if _item_administrable_products:
                    _items.append(_item_administrable_products.to_dict())
            _dict['administrableProducts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in medical_devices (list)
        _items = []
        if self.medical_devices:
            for _item_medical_devices in self.medical_devices:
                if _item_medical_devices:
                    _items.append(_item_medical_devices.to_dict())
            _dict['medicalDevices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in product_organization_roles (list)
        _items = []
        if self.product_organization_roles:
            for _item_product_organization_roles in self.product_organization_roles:
                if _item_product_organization_roles:
                    _items.append(_item_product_organization_roles.to_dict())
            _dict['productOrganizationRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudyVersionOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "versionIdentifier": obj.get("versionIdentifier"),
            "rationale": obj.get("rationale"),
            "documentVersionIds": obj.get("documentVersionIds"),
            "dateValues": [GovernanceDateOutput.from_dict(_item) for _item in obj["dateValues"]] if obj.get("dateValues") is not None else None,
            "amendments": [StudyAmendmentOutput.from_dict(_item) for _item in obj["amendments"]] if obj.get("amendments") is not None else None,
            "businessTherapeuticAreas": [Code.from_dict(_item) for _item in obj["businessTherapeuticAreas"]] if obj.get("businessTherapeuticAreas") is not None else None,
            "studyIdentifiers": [StudyIdentifier.from_dict(_item) for _item in obj["studyIdentifiers"]] if obj.get("studyIdentifiers") is not None else None,
            "referenceIdentifiers": [ReferenceIdentifier.from_dict(_item) for _item in obj["referenceIdentifiers"]] if obj.get("referenceIdentifiers") is not None else None,
            "studyDesigns": [SearchStudyDesignV3StudyDesignsGet200ResponseInner.from_dict(_item) for _item in obj["studyDesigns"]] if obj.get("studyDesigns") is not None else None,
            "titles": [StudyTitle.from_dict(_item) for _item in obj["titles"]] if obj.get("titles") is not None else None,
            "criteria": [EligibilityCriterionOutput.from_dict(_item) for _item in obj["criteria"]] if obj.get("criteria") is not None else None,
            "narrativeContentItems": [NarrativeContentItem.from_dict(_item) for _item in obj["narrativeContentItems"]] if obj.get("narrativeContentItems") is not None else None,
            "abbreviations": [AbbreviationOutput.from_dict(_item) for _item in obj["abbreviations"]] if obj.get("abbreviations") is not None else None,
            "roles": [StudyRole.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "organizations": [OrganizationOutput.from_dict(_item) for _item in obj["organizations"]] if obj.get("organizations") is not None else None,
            "administrableProducts": [AdministrableProductOutput.from_dict(_item) for _item in obj["administrableProducts"]] if obj.get("administrableProducts") is not None else None,
            "medicalDevices": [MedicalDeviceOutput.from_dict(_item) for _item in obj["medicalDevices"]] if obj.get("medicalDevices") is not None else None,
            "productOrganizationRoles": [ProductOrganizationRole.from_dict(_item) for _item in obj["productOrganizationRoles"]] if obj.get("productOrganizationRoles") is not None else None,
            "notes": [CommentAnnotation.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "instanceType": obj.get("instanceType")
        })
        return _obj


