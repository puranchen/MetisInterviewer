from enum import Enum

class DiagnosticCertainty(Enum):
    """The level of confidence in the identification of the diagnosis.
    
    Comment: If an alternative valueset is required, these values can be added to the DV_TEXT data type in a template."""
    SUSPECTED = "suspected"
    PROBABLE = "probable"
    CONFIRMED = "confirmed"

__all__ = ['DiagnosticCertainty']