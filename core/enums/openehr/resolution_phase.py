from enum import Enum

class ResolutionPhase(Enum):
    """Phase of healing for an acute problem or diagnosis.
    
    Comment: For example: tracking the progress of resolution of a middle ear infection.
    """
    NOT_RESOLVING = "not_resolving" #Problem or diagnosis is not progressing satisfactorily through the normal stages of restoration or healing towards resolution.
    RESOLVING = "resolving" 
    RESOLVED = "resolved"
    INDETERMINATE = "indeterminate" 
    RELAPSED = "relapsed" 

__all__ = ['ResolutionPhase']