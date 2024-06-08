from question import MultipleChoice, QuestionBool, QuestionFloat
from enum import Enum

# Questions
qHaveFever = MultipleChoice(prompt='Har du feber?', choices=['Ja', 'Nej', 'Vet ej/kanske'], lang='sv', none_option=False)
qBodyTemperature = QuestionFloat(prompt='Vad är din kroppstemperatur?', lang='sv', skippable=True, unit="ºC", min_value=20, max_value=55)
qCanMeasureTemp = QuestionBool(prompt='Har du möjlighet att mäta temperaturen?', lang='sv')
qFeelingWarm = QuestionBool(prompt='Känner du dig varm?', lang='sv')
qKnownImmunoDeficiency = QuestionBool(prompt='Har du någon känd immunbristsjukdom?', lang='sv')

class Fever(Enum):
    UNKNOWN = -1
    RULED_OUT = 0
    N_A = 1
    INCONCLUSIVE = 2
    CONFIRMED = 3

def assessFever(lang='sv'):
    
    # Root node: First question in the Fever assessment flowchart
    qHaveFever.ask(lang=lang)

    # Yes, have fever
    if qHaveFever.answer[0].idx == 1: 
        qBodyTemperature.ask(lang)
        if qBodyTemperature.answer is not None and qBodyTemperature.answer >= 38:
            return Fever.CONFIRMED
        elif qBodyTemperature.answer is not None and qBodyTemperature.answer in range(0, 38):
            qKnownImmunoDeficiency.ask(lang)
            if qKnownImmunoDeficiency.answer:
                return Fever.N_A
            else:
                return Fever.RULED_OUT
        else:
            qBodyTemperature.set_answer(None)

    # No, don't have fever
    elif qHaveFever.answer[0].idx == 2: 
        qKnownImmunoDeficiency.ask(lang)
        if qKnownImmunoDeficiency.answer:
            return Fever.N_A
        else:
            return Fever.RULED_OUT
        
    # Don't know/Maybe fever
    elif qHaveFever.answer[0].idx == 3: 
        qCanMeasureTemp.ask(lang)
        if qCanMeasureTemp.answer:
            qBodyTemperature.ask(lang)
            if qBodyTemperature.answer >= 38:
                return Fever.CONFIRMED
            elif qBodyTemperature.answer in range(0, 38):
                qKnownImmunoDeficiency.ask(lang)
                if qKnownImmunoDeficiency.answer:
                    return Fever.N_A
                else:
                    return Fever.RULED_OUT
            else:
                qBodyTemperature.set_answer(None)
        elif qCanMeasureTemp.answer == False:
            qFeelingWarm.ask(lang)
            if qFeelingWarm.answer:
                qKnownImmunoDeficiency.ask(lang)
                if qKnownImmunoDeficiency.answer:
                    return Fever.N_A
                else:
                    return Fever.INCONCLUSIVE
            else:
                qKnownImmunoDeficiency.ask(lang)
                if qKnownImmunoDeficiency.answer:
                    return Fever.N_A
                else:
                    return Fever.RULED_OUT
    else:
        raise ValueError('Something went wrong...')
    
