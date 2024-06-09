from enum import Enum

class Laterality(Enum):
    """Simple laterality of the anatomical location."""
    LEFT = "left"
    RIGHT = "right"
    BILATERAL = "bilateral"
    UNKNOWN = None

__all__ = ['Laterality']