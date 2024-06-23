from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class ArchetypeABC(ABC):
    """
    Abstract base class for all archetypes.
    """
    archetype_id: str
    concept_name: str
    concept_description: str
    keywords: List[str]
    purpose: str
    use: str
    misuse: str
    references: str