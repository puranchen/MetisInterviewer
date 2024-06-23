from question.question_int import QuestionInt
from enum import Enum
import yaml

class Pain(Enum):
    NONE = 0
    VERY_MILD = 1
    MILD = 2
    MODERATE = 3
    SEVERE = 4
    VERY_SEVERE = 5
    WORST_PAIN = 6
    UNKNOWN = -1


with open('core/assessment/painConfig.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

    qs = [d for d in data if d["type"] == 'question']
    es = [d for d in data if d["type"] == 'exit']

# initialize all questions and exits
Q = {}
for q in qs:
    Q[q.get('name')] = globals()[q.get('class_')](**q)
    
def evalPain(lang):

    Q['painLevel'].ask(lang)

    if Q['painLevel'].answer == 0:
        return Pain.NONE
    elif Q['painLevel'].answer <= 2:
        return Pain.VERY_MILD
    elif Q['painLevel'].answer <= 4:
        return Pain.MILD
    elif Q['painLevel'].answer == 5:
        return Pain.MODERATE
    elif Q['painLevel'].answer <= 7:
        return Pain.SEVERE
    elif Q['painLevel'].answer <= 9:
        return Pain.VERY_SEVERE
    elif Q['painLevel'].answer == 10:
        return Pain.WORST_PAIN
    else:
        print("SOMETHING WENT WRONG")
        return Pain.UNKNOWN
    
if __name__ == '__main__':
    evaluation = evalPain(lang='sv')
    print("\neval metadata:", evaluation.__dict__)
    print(f"{'='*100}\n")