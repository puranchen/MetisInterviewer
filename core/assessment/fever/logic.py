from assessment.condition_logic import ConditionLogic

if __name__ == "__main__":
    tree = ConditionLogic('config.yaml')
    outcome = tree.run()
    print("="*50)
    print(outcome)

