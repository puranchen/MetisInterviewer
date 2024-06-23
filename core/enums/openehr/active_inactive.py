from enum import Enum

class ActiveInactive(Enum):
    """Category that supports division of problems and diagnoses into Active or Inactive problem lists.
    
    Used in: problem_diagnosis_qualifier
    Comment: The Active/Inactive and Current/Past data elements have similar clinical impact but represent slightly different semantics. Both are actively used in different clinical settings, but usually not together. If a Current/Past qualifier is recorded, then this data element is likely to be redundant. An exception where a condition can be current but inactive is asthma that is not causing acute symptoms.
    """
    ACTIVE = 'active' #The problem or diagnosis is currently active and clinically relevant.
    INACTIVE = 'inactive' #The problem or diagnosis is not completely resolved but is inactive or felt less relevant to the current clinical context.

__all__ = ['ActiveInactive']