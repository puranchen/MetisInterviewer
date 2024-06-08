from enum import Enum
from question import MultipleChoice, QuestionBool

# Outcomes
class ConstitutionalSymptoms(Enum):
    NONE = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3
    UNKNOWN = -1

def assessConstitutionalSymptoms(lang='sv'):
    
    # Questions
    constSympt = MultipleChoice(
        prompt='Vilka av följande symptom stämmer in på dig?',
        choices=[
            'Blek, gråaktig eller blåvit hud',
            'Kallsvettig',
            'Orolig och rastlös',
            'Andfådd eller andas snabbt och ytligt',
            'Slö, dåsig och kraftlös',
            'Frossa (kraftiga, okontrollerade skakningar med samtidig frysningskänsla)',
        ],
        none_prompt='Inget av ovanstående',
        variant='multi-select',
        lang='sv'
    )

    notSelfSustaining = QuestionBool(
        prompt='Upplever du svårigheter att ta hand om dig själv?',
        lang='sv'
    )

    # Decision Tree
    constSympt.ask(lang)
    if len(set(constSympt.answer)) >= 3:
        return ConstitutionalSymptoms.SEVERE
    elif any(a.idx >= 1 for a in constSympt.answer):
        notSelfSustaining.ask(lang)
        if notSelfSustaining.answer:
            return ConstitutionalSymptoms.MODERATE
        else:
            return ConstitutionalSymptoms.MILD
    elif len(constSympt.answer) == 0:
        return ConstitutionalSymptoms.NONE
    else:
        return ConstitutionalSymptoms.UNKNOWN