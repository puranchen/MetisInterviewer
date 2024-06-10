from enum import Enum

class SeverityCategory(Enum):
    """Category representing the overall severity of the symptom or sign."""
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"


__all__ = ['SeverityCategory']