from question import QuestionInt
from enum import Enum

class Pain(Enum):
    NONE = 0
    VERY_MILD = 1
    MILD = 2
    MODERATE = 3
    SEVERE = 4
    VERY_SEVERE = 5
    WORST_PAIN = 6
    UNKNOWN = -1


qPain = QuestionInt(
    prompt="Hur skulle du beskriva din smärta på en skala från 0 till 10 där 0 är ingen smärta och 10 är värsta tänkbara smärta?",
    lang='sv',
    min_value=0,
    max_value=0
)
def assessPain():

    qPain.ask()

    if qPain.answer == 0:
        return Pain.NONE
    elif qPain.answer <= 2:
        return Pain.VERY_MILD
    elif qPain.answer <= 4:
        return Pain.MILD
    elif qPain.answer == 5:
        return Pain.MODERATE
    elif qPain.answer <= 7:
        return Pain.SEVERE
    elif qPain.answer <= 9:
        return Pain.VERY_SEVERE
    elif qPain.answer == 10:
        return Pain.WORST_PAIN
    else:
        print("SOMETHING WENT WRONG")
        return Pain.UNKNOWN