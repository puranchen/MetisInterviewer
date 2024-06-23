from enum import Enum
from question.multiple_choice import MultipleChoice
from question.question_float import QuestionFloat
from question.question_bool import QuestionBool
from core.enums.evals import Fever
import yaml
from assessment.constitutionalSymptomsLogic import evalConstitutionalSymptoms
from exits.exit_abc import ExitABC

with open('core/flowchart/dizzinessConfig.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

    qs = [d for d in data if d["type"] == 'question']
    es = [d for d in data if d["type"] == 'exit']

# initialize all questions and exits
Q = {}
for q in qs:
    Q[q.get('name')] = globals()[q.get('class_')](**q)

EXIT = {}
for e in es:
    EXIT[e.get('name')] = ExitABC(**e)

def evalDizziness(lang):
    Q['ongoingDizziness'].ask(lang)
    if Q['ongoingDizziness'].answer:
        Q['suddenDizziness'].ask(lang)
        Q['severeDizziness'].ask(lang)
        if any(a.idx in [1, 2, 3] for a in Q['severeDizziness'].answer):
            return EXIT['constitutionalSymptomsOrSevereDizziness']
        else:
            constitutionalSymptoms = evalConstitutionalSymptoms(lang)
            if constitutionalSymptoms.value >= 2: # >= Moderate
                return EXIT['constitutionalSymptomsOrSevereDizziness']
            else:
                Q['severeSymptomsWithDizziness'].ask(lang)
                if any(q.idx in [1, 2] for q in Q['severeSymptomsWithDizziness'].answer):
                    return EXIT['symptomFromChestWithDizziness']
                elif any(q.idx in [3] for q in Q['severeSymptomsWithDizziness'].answer):
                    return EXIT['symptomFromEarWithDizziness']
                elif any(q.idx in [4] for q in Q['severeSymptomsWithDizziness'].answer):
                    if Q['suddenDizziness'].answer:
                        return EXIT['suddenDizzinessWithHeadache']
                    else:
                        return neurologicalSymptomsWithDizziness_subtree(lang)
                elif any(q.idx in [5] for q in Q['severeSymptomsWithDizziness'].answer):
                    return EXIT['symptomFromEarWithDizziness']
                else:
                    return neurologicalSymptomsWithDizziness_subtree(lang)
    else:
        Q['dizzinessLastWeek'].ask(lang)
        if Q['dizzinessLastWeek'].answer:
            Q['severeSymptomsWithDizziness'].ask(lang)
            if any(q.idx in [1, 2] for q in Q['severeSymptomsWithDizziness'].answer):
                return EXIT['symptomFromChestWithDizziness']
            elif any(q.idx in [3] for q in Q['severeSymptomsWithDizziness'].answer):
                return EXIT['symptomFromEarWithDizziness']
            elif any(q.idx in [4] for q in Q['severeSymptomsWithDizziness'].answer):
                if Q['suddenDizziness'].answer:
                    return EXIT['suddenDizzinessWithHeadache']
                else:
                    return neurologicalSymptomsWithDizziness_subtree(lang)
            elif any(q.idx in [5] for q in Q['severeSymptomsWithDizziness'].answer):
                return EXIT['symptomFromEarWithDizziness']
            else:
                return neurologicalSymptomsWithDizziness_subtree(lang)
        else:
            return certainMovementsAndDizziness_subtree(lang)

def neurologicalSymptomsWithDizziness_subtree(lang):
    Q['neurologicalSymptomsWithDizziness'].ask(lang)
    if any(q.idx != 0 for q in Q['neurologicalSymptomsWithDizziness'].answer):
        Q['symptomsPassed'].ask(lang)
        if Q['symptomsPassed'].answer:
            return EXIT['neurologicalSymptomsWithDizziness']
        else:
            return EXIT['neurologicalSymptomsWithDizzinessResolved']
    else:
        return certainMovementsAndDizziness_subtree(lang)
    
    
def certainMovementsAndDizziness_subtree(lang):
    Q['certainMovementsAndDizziness'].ask(lang)
    if Q['certainMovementsAndDizziness']:
        return EXIT['certainMovementsDizziness']
    else:
        Q['moderateSymptomsWithDizziness'].ask(lang)
        if any(q.idx != 0 for q in Q['moderateSymptomsWithDizziness'].answer):
            Q['mildSymptomsWithDizziness'].ask(lang)
            if any(q.idx == 1 for q in Q['mildSymptomsWithDizziness'].answer):
                return EXIT['dizzinessAfterSeaTravel']
            elif any(q.idx == 2 for q in Q['mildSymptomsWithDizziness'].answer):
                return EXIT['occasionalDizziness']
            else:
                return EXIT['safetyExitDizziness']
            
# Entry point            
def main():
    return evalDizziness('sv')

if __name__ == '__main__':
    response = main()
    print(response.__dict__)