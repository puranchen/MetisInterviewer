from openEHR.archetypes.entry.observation import BodyTemperature
from openEHR.archetypes.cluster import SymptomSign

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Patient(metaclass=SingletonMeta):
    def __init__(self):
        self.symptom_signs_collection = []
        self.observation_collection = []
        self.evaluation_collection = []

    def add_symptom_sign(self, symptom_sign: SymptomSign):
        if isinstance(symptom_sign, SymptomSign):
            self.symptom_signs_collection.append(symptom_sign)
        else:
            raise ValueError(f"Invalid value for symptom_sign: {symptom_sign!r}")

    def add_observation(self, observation: BodyTemperature):
        self.observation_collection.append(observation)
        
    def add_evaluation(self, evaluation):
        self.evaluation_collection.append(evaluation)

    def __repr__(self):
        return f'Patient(symptom_signs_collection={self.symptom_signs_collection})'