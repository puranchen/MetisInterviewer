from enum import Enum
from core.question.question import MultipleChoice, QuestionBool, QuestionFloat
from core.enums.evals import Fever

# Questions
qHaveFever = MultipleChoice(prompt='Har du feber?', choices=['Ja', 'Nej', 'Vet ej/kanske'], lang='sv', none_option=False)
qBodyTemperature = QuestionFloat(prompt='Vad är din kroppstemperatur?', lang='sv', skippable=True, unit="ºC", min_value=20, max_value=55)
qCanMeasureTemp = QuestionBool(prompt='Har du möjlighet att mäta temperaturen?', lang='sv')
qFeelingWarm = QuestionBool(prompt='Känner du dig varm?', lang='sv')
qKnownImmunoDeficiency = QuestionBool(prompt='Har du någon känd immunbristsjukdom?', lang='sv')

def immsupp_subtree(lang, else_=Fever.RULED_OUT):
    qKnownImmunoDeficiency.ask(lang)
    if qKnownImmunoDeficiency.answer:
        return Fever.N_A
    else:
        return else_

def body_temp_subtree(lang):
    qBodyTemperature.ask(lang)
    if qBodyTemperature.answer is not None and qBodyTemperature.answer >= 38:
        return Fever.CONFIRMED
    elif qBodyTemperature.answer is not None and qBodyTemperature.answer in range(0, 38):
        return immsupp_subtree(lang)
    else:
        qBodyTemperature.set_answer(None)
        return None

def assess_fever(lang='sv'):
    """ Decision tree for assessing fever. """

    # Root node: First question in the Fever assessment flowchart
    qHaveFever.ask(lang)

    # Yes, have fever
    if qHaveFever.answer[0].idx == 1: 
        aBodyTempResponse = body_temp_subtree(lang)
        if aBodyTempResponse is not None:
            return aBodyTempResponse

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
            aBodyTempResponse = body_temp_subtree(lang)
            if aBodyTempResponse is not None:
                return aBodyTempResponse
        elif qCanMeasureTemp.answer == False:
            qFeelingWarm.ask(lang)
            if qFeelingWarm.answer:
                immsupp_subtree(lang, Fever.INCONCLUSIVE)
            else:
                return immsupp_subtree(lang)
    else:
        raise ValueError('Something went wrong...')
    
