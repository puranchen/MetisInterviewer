from enum import Enum

class Episodicity(Enum):
    """
    New: A new episode of the symptom or sign - either the first ever occurrence or a reoccurrence where the previous episode had completely resolved.
    Ongoing: This symptom or sign is ongoing, effectively a single, continuous episode.
    Indeterminate: It is not possible to determine if this occurrence of the symptom or sign is new or ongoing.
    """

    NEW = 'new'
    ONGOING = 'ongoing'
    INDETERMINATE = 'indeterminate'