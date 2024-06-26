import yaml
from question.question_bool import QuestionBool
from question.multiple_choice import MultipleChoice
from enum import Enum

# Outcomes
class ConstitutionalSymptoms(Enum):
    NONE = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3
    UNKNOWN = -1

with open('core/assessment/constitutionalSymptomsConfig.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

    qs = [d for d in data if d["type"] == 'question']
    es = [d for d in data if d["type"] == 'exit']

# initialize all questions and exits
Q = {}
for q in qs:
    Q[q.get('name')] = globals()[q.get('class_')](**q)

def evalConstitutionalSymptoms(lang='sv'):
    
    # Decision Tree
    Q["constitutionalSymptoms"].ask(lang)
    if len(set(Q["constitutionalSymptoms"].answer)) >= 3:
        return ConstitutionalSymptoms.SEVERE
    elif all(q.idx != 0 for q in Q["constitutionalSymptoms"].answer):
        Q["notSelfSustaining"].ask(lang)
        if Q["notSelfSustaining"].answer:
            return ConstitutionalSymptoms.MODERATE
        else:
            return ConstitutionalSymptoms.MILD
    elif all(q.idx == 0 for q in Q["constitutionalSymptoms"].answer):
        return ConstitutionalSymptoms.NONE
    else:
        return ConstitutionalSymptoms.UNKNOWN
    
if __name__ == '__main__':
    evaluation = evalConstitutionalSymptoms('sv')
    print("\neval metadata:", evaluation.__dict__)
    print(f"{'='*100}\n")