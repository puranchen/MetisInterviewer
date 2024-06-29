import networkx as nx
import yaml
from question import *
from enum import Enum

# Outcomes
class ConstitutionalSymptoms(Enum):
    NONE = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3
    UNKNOWN = -1

class Fever(Enum):
    UNKNOWN = -1
    RULED_OUT = 0
    N_A = 1
    INCONCLUSIVE = 2
    CONFIRMED = 3

class Pain(Enum):
    NO_PAIN = 0
    VERY_MILD = 1
    MILD = 2
    MODERATE = 3
    SEVERE = 4
    VERY_SEVERE = 5
    WORST_PAIN = 6
    UNKNOWN = -1
    
class ConditionLogic:

    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        self.graph = nx.DiGraph()
        self.start_node = config['nodes'][0].get('id')
        self.current_node = self.start_node
        self.Q = {}
        self.EXIT = {}
        self.EVAL = {}
        self.id_to_node = {}
        self.node_to_id = {}
        self.load_tree(config)

    def load_tree(self, config):
        nodes = config['nodes']

        for node in nodes:
            if node.get('type') == 'question':
                node_object = globals()[node.get('class')](**node)
            
                self.graph.add_node(node_object)
                self.id_to_node[node.get('id')] = node_object  # Populate the mapping

            if node.get('type') == 'evaluation':
                function_string = node.get('func')
                exec(function_string, globals())
                self.id_to_node[node.get('id')].evaluate = evaluate
                
        self.node_to_id = {node:id for id, node in self.id_to_node.items()}

    def run(self, lang='sv'):
        node_object = self.id_to_node[self.start_node]
        self.current_node = node_object
        while True:
            self.current_node.ask(lang)
            response = self.current_node.evaluate()
            if isinstance(response, Enum):
                return response
            elif isinstance(response, str):
                self.current_node = self.id_to_node[response]
        