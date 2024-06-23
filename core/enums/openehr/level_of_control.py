from enum import Enum

class LevelOfControl(Enum):
    """Category of the level of control of the problem or diagnosis by the current management."""
    CONTROLLED = "controlled" #The problem or diagnosis is controlled by current management.
    INDETERMINATE = "indeterminate" #It is not possible to determine if the problem or diagnosis is controlled by current management.
    NOT_CONTROLLED = "not_controlled" #The problem or diagnosis is not controlled by current management.

__all__ = ['LevelOfControl']