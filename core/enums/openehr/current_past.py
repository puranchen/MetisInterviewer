from enum import Enum

class CurrentPast(Enum):
    """Category that supports division of problems and diagnoses into Current or Past problem lists.

    Used in: problem_diagnosis_qualifier
    Comment: The Current/Past and Active/Inactive data elements have similar clinical impact but represent slightly different semantics. Both are actively used in different clinical settings, but usually not together. If an Active/Inactive qualifier is recorded, then this data element is likely to be redundant. An exception where a condition can be current but inactive is asthma that is not causing acute symptoms.
    """
    CURRENT = "current" #An issue occuring at present.
    PAST = "past" #An issue which ocurred in the past.

__all__ = ['CurrentPast']