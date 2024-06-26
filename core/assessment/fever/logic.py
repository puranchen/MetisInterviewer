from enum import Enum
from question import *
from core.enums.evals import Fever
import yaml

with open('core/assessment/feverConfig.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

    qs = [d for d in data if d["type"] == 'question']
    es = [d for d in data if d["type"] == 'exit']

# initialize all questions and exits
Q = {}
for q in qs:
    Q[q.get('name')] = globals()[q.get('class_')](**q)


def immsupp_subtree(lang, else_=Fever.RULED_OUT):
    Q["KnownImmunoDeficiency"].ask(lang)
    if Q["KnownImmunoDeficiency"].answer:
        return Fever.N_A
    else:
        return else_

def body_temp_subtree(lang):
    Q["bodyTemperature"].ask(lang)
    if Q["bodyTemperature"].answer is not None and Q["bodyTemperature"].answer >= 38:
        return Fever.CONFIRMED
    elif Q["bodyTemperature"].answer is not None and Q["bodyTemperature"].answer in range(0, 38):
        return immsupp_subtree(lang)
    else:
        Q["bodyTemperature"].set_answer(None)
        return None

def evalFever(lang='sv'):
    """ Decision tree for assessing fever. """

    # Root node: First question in the Fever assessment flowchart
    Q["haveFever"].ask(lang)

    # Yes, have fever
    if Q["haveFever"].answer[0].idx == 1: 
        aBodyTempResponse = body_temp_subtree(lang)
        if aBodyTempResponse is not None:
            return aBodyTempResponse

    # No, don't have fever
    elif Q["haveFever"].answer[0].idx == 2: 
        Q["knownImmunoDeficiency"].ask(lang)
        if Q["knownImmunoDeficiency"].answer:
            return Fever.N_A
        else:
            return Fever.RULED_OUT
        
    # Don't know/Maybe fever
    elif Q["haveFever"].answer[0].idx == 3: 
        Q["canMeasureTemp"].ask(lang)
        if Q["canMeasureTemp"].answer:
            aBodyTempResponse = body_temp_subtree(lang)
            if aBodyTempResponse is not None:
                return aBodyTempResponse
        elif Q["canMeasureTemp"].answer == False:
            Q["feelingWarm"].ask(lang)
            if Q["feelingWarm"].answer:
                immsupp_subtree(lang, Fever.INCONCLUSIVE)
            else:
                return immsupp_subtree(lang)
    else:
        raise ValueError('Something went wrong...')
    
if __name__ == '__main__':
    evaluation = evalFever('sv')
    print("\neval metadata:", evaluation.__dict__)
    print(f"{'='*100}\n")