from enums import CurrentPast, DiagnosticStatus, ActiveInactive, Progression, Episodicity, Occurrence, LevelOfControl, ResolutionPhase
from utils import enum_property

class ProblemDiagnosisQualifier:
    def __init__(self, **kwargs):
        self.diagnostic_status = kwargs.get('diagnostic_status', None)
        self.current_past = kwargs.get('current_past', None)
        self.active_inactive = kwargs.get('active_inactive', None)
        self.level_of_control = kwargs.get('level_of_control', None)
        self.progression = kwargs.get('progression', None)
        self.resolution_phase = kwargs.get('resolution_phase', None)
        self.remission_status = kwargs.get('remission_status', None)
        self.episodicity = kwargs.get('episodicity', None)
        self.reason_for_an_ongoing_episode = kwargs.get('reason_for_an_ongoing_episode', None)
        self.occurrence = kwargs.get('occurrence', None)
        self.course_label = kwargs.get('course_label', None)
        self.diagnostic_category = kwargs.get('diagnostic_category', None)
        self.admission_diagnosis = kwargs.get('admission_diagnosis', None)
        self.comment = kwargs.get('comment', None)

    diagnostic_status = enum_property(DiagnosticStatus)
    current_past = enum_property(CurrentPast)
    active_inactive = enum_property(ActiveInactive)
    level_of_control = enum_property(LevelOfControl)
    progression = enum_property(Progression)
    resolution_phase = enum_property(ResolutionPhase)
    episodicity = enum_property(Episodicity)
    occurrence = enum_property(Occurrence)

    def __repr__(self):
        return f"ProblemDiagnosisQualifier({self.__dict__!r})"
    