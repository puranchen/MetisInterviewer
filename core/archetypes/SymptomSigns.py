"""
Adaptation of the SymptomSign Archetype from openEHR

Information:
openEHR-EHR-CLUSTER.symptom_sign.v2
Original namespace: org.openehr
Original publisher: openEHR Foundation
Revision: 2.1.1 (published)

Build UID: 74cfa31e-e26e-4fe9-8101-a52864cad6f1
Major Version UID: 88c7d677-fa69-498f-aec2-976c53d15a6f
Canonical MD5 Hash: FCE561F6A986DB8BAAAA657711F52D16
"""

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional, List
from archetypes import AnatomicalLocation
from enums import SeverityCategory

class SymptomSign(BaseModel):
    """Reported observation of a physical or mental disturbance in an individual."""
    name: str = Field(..., description="Simple name of the symptom or sign")
    structured_anatomical_location: str = Field(..., description="Structured body site where the symptom or sign was reported.")
    negated: bool = Field(False, description="Whether the symptom or sign was negated.")

class SymptomSigns(BaseModel):
    symptom_signs: List[SymptomSign]

__all__ = ['SymptomSigns']