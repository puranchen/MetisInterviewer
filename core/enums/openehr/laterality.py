from enum import Enum

class Laterality(Enum):
    """
    The side of the body on which the identified body site is located.
    
    Comment: If the identified body site has no laterality, this data element should not have a value. If the 'Body site name' data element uses pre-coordinated terms that include laterality, then this data element is redundant.
    """
    LEFT = "left"
    RIGHT = "right"

__all__ = ['Laterality']