from enum import Enum

class DiagnosticStatus(Enum):
    PRELIMINARY = 'preliminary'
    WORKING = 'working'
    ESTABLISHED = 'established'
    REFUTED = 'refuted'

__all__ = ['DiagnosticStatus']