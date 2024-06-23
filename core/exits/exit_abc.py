from abc import ABC
from enum import Enum

class RGSExit(Enum):
    """Enum for the different types of RGS exits."""
    IMMEDIATE = 1
    PROMPTLY = 2
    ACUTE = 3
    PLANNED = 4
    WAIT = 5

class NTSExit(Enum):
    """Enum for the different types of NTS exits."""
    IMMEDIATE = 1
    PROMPTLY = 2
    ACUTE = 3
    PLANNED = 4
    WAIT = 5

EXIT_SCHEMA = {'rgs': RGSExit, 'nts': NTSExit}

class ExitABC(ABC):
    """Base class for all exits."""
    
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.description = kwargs.get('desc', None)
        self.schema = kwargs.get('schema', None)
        self.urgency = kwargs.get('urgency')

    @property
    def urgency(self):
        """ Get the urgency of the exit. """
        return self._urgency
    
    @urgency.setter
    def urgency(self, value):
        """ Set the urgency of the exit. """
        exit_schema = EXIT_SCHEMA[self.schema]
        if not isinstance(value, exit_schema):
            if isinstance(value, str):
                value = exit_schema[value.upper()]
            else:
                raise ValueError("Urgency must be an ExitEnum or a string.")
        self._urgency = value