from openEHR.archetypes.cluster.problem_diagnosis_qualifier import ProblemDiagnosisQualifier
from openEHR.archetypes.cluster.anatomical_location import AnatomicalLocation
from utils import class_property, enum_property
from enums import Severity, DiagnosticCertainty

class ProblemDiagnosis:
    def __init__(self, name, **kwargs):
        self.name = name
        self.variant = kwargs.get('variant', None)
        self.clinical_description = kwargs.get('clinical_description', None)
        self.body_site = kwargs.get('body_site', None)
        self.structured_body_site = kwargs.get('structured_body_site', None)
        self.cause = kwargs.get('cause', None)
        self.datetime_of_onset = kwargs.get('datetime_of_onset', None)
        self.datetime_clinically_recognised = kwargs.get('datetime_clinically_recognised', None)
        self.severity = kwargs.get('severity', None)
        self.specific_details = kwargs.get('specific_details', None)
        self.course_description = kwargs.get('course_description', None)
        self.datetime_of_resolution = kwargs.get('datetime_of_resolution', None)
        self.status = kwargs.get('status', None)
        self.diagnostic_certainty = kwargs.get('diagnostic_certainty', None)
        self.comment = kwargs.get('comment', None)

    structured_body_site = class_property(AnatomicalLocation)
    severity = enum_property(Severity)
    status = class_property(ProblemDiagnosisQualifier)
    diagnostic_certainty = enum_property(DiagnosticCertainty)

    def __repr__(self):
        return f"ProblemDiagnosis({self.__dict__!r})"
    
__all__ = ['ProblemDiagnosis']