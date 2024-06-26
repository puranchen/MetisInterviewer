"""
Adaptation of the SymptomSign Archetype from openEHR

Information:
openEHR-EHR-CLUSTER.anatomical_location.v1
Original namespace: org.openehr
Original publisher: openEHR Foundation
Revision: 1.2.2 (published)

Build UID: 13ee6d25-aa99-4221-bdc1-3c7ee7e58795
Major Version UID: 2fe9e9f8-adfd-4406-878a-82b38ef498a9
Canonical MD5 Hash: 62823A86BC1C2B02574125E21F5DECCB

### Concept Description
A physical site on or within the human body.

### Keywords
location, site, anatomical, anatomic region, topographic anatomy, macroscopic, anatomic, anatomy

### Purpose
To identify and record structured details about a single physical site on, or within, the human body using macroscopic anatomical terms.

### Use
Use to record structured and consistent details about a single identified physical site on, or within, the human body.

This archetype is specifically designed to be used within the context of any appropriate ENTRY or CLUSTER archetypes which supply the context of the anatomical location.

As a fundamental part of clinical practice, clinicians can describe anatomical locations in a myriad of complex and variable ways. In practice, some archetypes carry a single data element for carrying a simple description of body site - for example, OBSERVATION.blood_pressure and CLUSTER.symptom when describing ear pain. In this situation, where the value set is predictable and simple to define, this single data element is a very accurate and pragmatic way to record the site in the body and to query at a later date. However in the situation where the anatomical location is not well defined or needs to be determined at run-time, it may be more flexible to use this structured archetype. For example, in the situation where any symptom can be recorded without any predefined scope of the type of symptom, then allowing the use of this archetype to specifically define an anatomical location in the body may be useful. In this case the CLUSTER.symptom archetype also carries a SLOT for 'Detailed anatomical location' which can include this archetype to support maximal flexibility in recording anatomical location data.

This archetype supports recording complex structured anatomical sites. For example, the apex beat of the heart is typically found at the fifth left intercostal space in the mid-clavicular line, tenderness at McBurney's point on the abdominal wall or a laceration on the palmar aspect of the proximal right thumb.

A combination of the data elements in this archetype can be used to individually record each component of a postcoordinated terminology expression that represents the anatomical site.

The 'Alternative structure' SLOT allows inclusion of additional archetypes that provide an alternative structure for describing the same body site, such as CLUSTER.anatomical_location_relative or CLUSTER.anatomical_location_clock, should this be required. In the situation where this archetype can only be used to name a large and/or non-specific body part, the additional use of the CLUSTER.anatomical_location_relative archetype will support recording of a more precise location - for example, 2 cm anterior to the cubital fossa of the left forearm or 4 cm below R costal margin on the chest wall in the mid-clavicular line.

If this archetype is used within other archetypes where the specified subject of care is not the individual for whom the record is being created, for example a fetus in-utero, then the anatomical location will be identifying a body site on or within the fetus.

### Misuse
Not to be used for specifiying unilateral/bilateral occurrences of an anatomical feature.

"""

from enums import Laterality, Aspect, AnatomicalLine
from utils import enum_property

class AnatomicalLocation:
    def __init__(self, name:str, **kwargs):
        self.name = name
        self.specific_site = kwargs.get('specific_site', None)
        self.laterality = kwargs.get('laterality', None)
        self.aspect = kwargs.get('aspect', None)
        self.anatomical_line = kwargs.get('anatomical_line', None)
        self.description = kwargs.get('description', None)
        self.alternative_structure = kwargs.get('alternative_structure', None)
        self.multimedia_representation = kwargs.get('multimedia_representation', None)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value.lower()
        else:
            raise ValueError(f"Invalid type for name: {value!r}")
        
    laterality = enum_property(Laterality)
    aspect = enum_property(Aspect)
    anatomical_line = enum_property(AnatomicalLine)

    def __repr__(self):
        return f"AnatomicalLocation({self.__dict__!r})"

__all__ = ['AnatomicalLocation']