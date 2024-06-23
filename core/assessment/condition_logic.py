import networkx as nx
import yaml
from question.question_bool import QuestionBool
from question.multiple_choice import MultipleChoice
from assessment.constitutionalSymptomsLogic import evalConstitutionalSymptoms
from exits.exit_abc import ExitABC

class ConditionLogic:
    def __init__(self, config):
        self.graph = nx.DiGraph()
        self.load_tree(config)
        self.current_node = 'ongoingDizziness' # start node
        self.Q = {}
        self.EXIT = {}
        self.EVAL = {}

    def load_tree(self, config):
        for node in config['nodes']:
            self.graph.add_node(node['id'], **node)
            


          