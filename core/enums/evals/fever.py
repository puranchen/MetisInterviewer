from enum import Enum

class Fever(Enum):
    UNKNOWN = -1
    RULED_OUT = 0
    N_A = 1
    INCONCLUSIVE = 2
    CONFIRMED = 3