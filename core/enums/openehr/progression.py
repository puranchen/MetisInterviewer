from enum import Enum

class Progression(Enum):

    WORSENING = 'worsening'
    UNCHANGED = 'unchanged'
    IMPROVING = 'improving'
    RESOLVED = 'resolved'

__all__ = ['Progression']