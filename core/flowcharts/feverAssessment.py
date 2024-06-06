from question import MultipleChoice, QuestionBool, QuestionFloat
from enum import Enum

# Questions
qHaveFever = MultipleChoice(prompt='Har du feber?', choices=['Ja', 'Nej', 'Vet ej/kanske'], lang='sv', none_option=False)
qBodyTemperature = QuestionFloat(prompt='Vad är din kroppstemperatur?', lang='sv', skippable=True)
qCanMeasureTemp = QuestionBool(prompt='Har du möjlighet att mäta temperaturen?', lang='sv')
qFeelingWarm = QuestionBool(prompt='Känner du dig varm?', lang='sv')
qKnownImmunoDeficiency = QuestionBool(prompt='Har du någon känd immunbristsjukdom?', lang='sv')

class Fever(Enum):
    UNKNOWN = 0
    CONFIRMED = 1
    RULED_OUT = 2
    N_A = 3
    INCONCLUSIVE = 4

def feverAssessment(lang='sv'):
    
    # Root node: First question in the Fever assessment flowchart
    qHaveFever.ask(lang=lang)

    if qHaveFever.answer.idx == 1: # Yes
        qBodyTemperature.ask(lang=lang)
        if qBodyTemperature.answer is not None and qBodyTemperature.answer >= 38:
            return Fever.CONFIRMED
        else:
            qKnownImmunoDeficiency.ask(lang=lang)
            if qKnownImmunoDeficiency.answer:
                return Fever.N_A
            else:
                return Fever.RULED_OUT
            
    elif qHaveFever.answer is not None and qHaveFever.answer.idx == 2: # No
        qKnownImmunoDeficiency.ask(lang=lang)
        if qKnownImmunoDeficiency.answer: # Known immunodeficiency
            return Fever.N_A
        else:
            return Fever.RULED_OUT
        
    elif qHaveFever.answer.idx == 3: # Don't know/Maybe
        qCanMeasureTemp.ask(lang=lang)
        if qCanMeasureTemp.answer: # Can measure temperature
            qBodyTemperature.ask(lang=lang)
            if qBodyTemperature.answer >= 38:
                return Fever.CONFIRMED
            else:
                qKnownImmunoDeficiency.ask(lang=lang)
                if qKnownImmunoDeficiency.answer:
                    return Fever.N_A
                else:
                    return Fever.RULED_OUT
        else: # Can't measure temperature
            qFeelingWarm.ask(lang=lang)
            if qFeelingWarm.answer: 
                qKnownImmunoDeficiency.ask(lang=lang)
                if qKnownImmunoDeficiency.answer:
                    return Fever.N_A
                else:
                    return Fever.INCONCLUSIVE
            else:
                qKnownImmunoDeficiency.ask(lang=lang)
                if qKnownImmunoDeficiency.answer:
                    return Fever.N_A
                else:
                    return Fever.RULED_OUT