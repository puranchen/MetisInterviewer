from langchain_core.pydantic_v1 import BaseModel, Field
from enums import Laterality

class AnatomicalLocation(BaseModel):
    """A physical site on or within the human body."""
    body_site_name: str = Field(..., description="Simple name of the anatomical location")
    laterality: Laterality = Field(Laterality.UNKNOWN, description="Simple laterality of the anatomical location")

__all__ = ['AnatomicalLocation']