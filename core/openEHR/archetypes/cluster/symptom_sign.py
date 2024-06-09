"""
Adaptation of the SymptomSign Archetype from openEHR

Information:
openEHR-EHR-CLUSTER.symptom_sign.v2
Original namespace: org.openehr
Original publisher: openEHR Foundation
Revision: 2.1.1 (published)

Build UID: 74cfa31e-e26e-4fe9-8101-a52864cad6f1
Major Version UID: 88c7d677-fa69-498f-aec2-976c53d15a6f
Canonical MD5 Hash: FCE561F6A986DB8BAAAA657711F52D16
"""

from typing import Optional
from enums import Episodicity

class SymptomSign:
    """Reported observation of a physical or mental disturbance in an individual."""
    def __init__(self, name:str, episodicity: Optional[Episodicity] = None):
        self.name = name
        self.episodicity  = episodicity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.lower()    
    
    @property
    def episodicity(self):
        return self._episodicity
    
    @episodicity.setter
    def episodicity(self, value):
        if value is not None:
            if isinstance(value, Episodicity):
                self._episodicity = value
            elif isinstance(value, str) and value.upper() in Episodicity.__members__:
                self._episodicity = Episodicity[value.upper()]
            else:
                raise ValueError(f"Invalid value for episodicity: {value!r}")
        else:
            self._episodicity = None

    def __repr__(self):
        return f"SymptomSign(name={self._name!r}, episodicity={self._episodicity!r})"