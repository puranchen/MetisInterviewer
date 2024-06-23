from typing import Optional
from enums import Episodicity, Laterality, Aspect, AnatomicalLine, Occurrence, Progression, SeverityCategory
from openEHR.archetypes.cluster.anatomical_location import AnatomicalLocation
from utils import enum_property

class SymptomSign:
    """Reported observation of a physical or mental disturbance in an individual."""
    def __init__(self, name, **kwargs):
        self.name = name
        self.body_site = kwargs.get("body_site", None)
        self.structured_body_site = kwargs.get("structured_body_site", None)
        self.description = kwargs.get("description", None)
        self.episodicity = kwargs.get("episodicity", None)
        self.occurrence = kwargs.get("occurrence", None)
        self.episode_onset = kwargs.get("episode_onset", None)
        self.onset_timing = kwargs.get("onset_timing", None)
        self.nadir = kwargs.get("nadir", None)
        self.episode_duration = kwargs.get("episode_duration", None)
        self.severity_category = kwargs.get("severity_category", None)
        self.severity_rating = kwargs.get("severity_rating", None)
        self.character = kwargs.get("character", None)
        self.progression = kwargs.get("progression", None)
        self.pattern = kwargs.get("pattern", None)
        #self.modifying_factor = kwargs.get("modifying_factor", None)
        #self.precipitating_factor = kwargs.get("precipitating_factor", None)
        #self.resolving_factor = kwargs.get("resolving_factor", None)
        self.impact = kwargs.get("impact", None)
        self.episode_description = kwargs.get("episode_description", None)
        self.specific_details = kwargs.get("specific_details", None)
        self.resolution_datetime = kwargs.get("resolution_datetime", None)
        self.description_of_previous_episodes = kwargs.get("description_of_previous_episodes", None)
        self.number_of_previous_episodes = kwargs.get("number_of_previous_episodes", None)
        self.previous_episodes = kwargs.get("previous_episodes", None)
        self.associated_symptom_sign = kwargs.get("associated_symptom_sign", None)
        self.comment = kwargs.get("comment", None)

    @property
    def name(self):
        return self._name

    @name.setter #TODO: convert this to a lookup function for SNOMEDCT terms, and enable using sctid to define SymptomSign. 
    def name(self, value):
        if isinstance(value, str): #Should probably be converted to a DV_CODED_TEXT class
            self._name = value.lower()    
        else:
            raise ValueError(f"Invalid type for name: {value!r}")
    
    episodicity = enum_property(Episodicity)
    occurrence = enum_property(Occurrence)
    severity_category = enum_property(SeverityCategory)
    progression = enum_property(Progression)

    def __repr__(self):
        return f"SymptomSign({self.__dict__!r})"

__all__ = ['SymptomSign']