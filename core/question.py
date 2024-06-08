from abc import ABC, abstractmethod

class QuestionABC(ABC):
    """ Base class for all questions. """
    def __init__(self, prompt:str, answer=None, lang:str='en', skippable=False, asked=False):
        self._prompt = {lang: prompt}
        self._answer = None
        if answer is not None:
            self.set_answer(answer)
        self.skippable = skippable
        self.asked = asked

    @property
    def prompt(self):
        return self._prompt
    
    @abstractmethod
    def set_prompt(self, value):
        pass

    @property
    def answer(self):
        return self._answer
    
    @abstractmethod
    def set_answer(self, value=None):
        pass
    


class QuestionBool(QuestionABC):
    """ Question with a boolean answer. """
    def set_answer(self, value=None):
        if value is not None:
            if not isinstance(value, bool) and not value in [0,1]:
                raise ValueError(f"Answer must be a boolean, got {type(value)}:")
            self._answer = bool(value)
    
    def set_prompt(self, value):
        self._prompt.update(value)

    def ask(self, lang='sv'):
        answer = ""
        while answer not in [1, 2]:
            print("")
            print(self.prompt.get(lang))
            print("1 - Ja\n2 - Nej")
            answer = int(input("Svar: "))
        self.set_answer(answer == 1)
        self.asked = True

    def __repr__(self):
        return f"QuestionBool(prompt={self.prompt!r}, answer={self._answer!r})"

class QuestionInt(QuestionABC):
    """ Question with an integer answer. """
    def set_answer(self, value=None):
        if value is not None:
            if not isinstance(value, int):
                raise ValueError(f"Answer must be an integer, got {type(value)}:")
            self._answer = int(value)
    
    def set_prompt(self, value):
        self._prompt.update(value)

    def ask(self, lang='sv'):
        answer = None
        while not answer.isdigit():
            print("")
            print(self.prompt.get(lang))
            answer = input("Svar: ")
        self.set_answer(int(answer))
        self.asked = True

    def __repr__(self):
        return f"QuestionInt(prompt={self.prompt!r}, answer={self._answer!r})"
    
class QuestionFloat(QuestionABC):
    """ Question with a float answer. """

    def __init__(self, prompt, unit, lang = 'en', min_value:float=None, max_value:float=None, skippable=False):
        super().__init__(prompt, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value

    def set_answer(self, value=None):
        if value is not None:
            if not isinstance(value, (float, int)):
                raise ValueError(f"Answer must be a float or int, got {type(value)}:")
            self._answer = float(value)
    
    def set_prompt(self, value):
        self._prompt.update(value)

    def ask(self, lang='sv'):
        answer = ""
        while not answer.replace(".", "").replace(",","").isdigit():
            print("")
            print(self.prompt.get(lang))    
            answer = input(f"Svar ({self.unit}): ")
            if not answer.replace(".", "").replace(",","").isdigit():
                print(f"Invalid answer: {answer!r}. Must be a number.")
                continue
            outside_limits = False
            if self.max_value is not None:
                if float(answer) > self.max_value:  
                    print(f"Value too large: {answer}. Must be a between {self.min_value!r} and {self.max_value!r}.")
                    outside_limits = True
            if self.min_value is not None:
                if float(answer) < self.min_value:
                    print(f"Value too small: {answer}. Must be a between {self.min_value!r} and {self.max_value!r}.")
                    outside_limits = True
            if outside_limits:
                answer = ""
                continue

        self.set_answer(float(answer.replace(",",".")))
        self.asked = True

    def __repr__(self):
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"
    
class QuestionStr(QuestionABC):
    """ Question with a string answer. """
    def set_answer(self, value=None):
        if value is not None:
            self._answer = str(value)
    
    def set_prompt(self, value):
        self._prompt.update(value)

    def ask(self, lang='sv'):
        print("")
        print("\n", self.prompt.get(lang))
        answer = input("Svar: ")
        self.set_answer(answer)
        self.asked = True

    def __repr__(self):
        return f"QuestionStr(prompt={self.prompt!r}, answer={self._answer!r})"
    
class MCOption(QuestionBool):
    """ Wrapper around QuestionBool for multiple choice options. """
    def __init__(self, idx, prompt:str, answer=None, lang:str='en'):
        super().__init__(prompt, answer, lang)
        self.idx = idx
    
    def __repr__(self):
        return f"MCOption(idx={self.idx!r}, prompt={self.prompt!r}, answer={self._answer!r})"

class MultipleChoice(QuestionABC):
    """ Question with multiple choice answers. """
    def __init__(self, prompt:str, choices:list, answer:list=None, lang:str='en', none_option=True, none_prompt="None of the above", mc_type='single-select', answered=False):
        super().__init__(prompt, answer, lang)
        self._choices = []
        self.none_option = none_option
        self.none_prompt = none_prompt
        self.mc_type = mc_type
        self._answered = False
        if answered:
            self.complete()
        self.set_choices(choices, lang)
        self._answer: list = []
        
    @property
    def choices(self):
        return self._choices
    
    def set_choices(self, choices: list, lang:str='en'):
        if all(isinstance(choice, str) for choice in choices):
            self._choices = [MCOption(idx+1, prompt=prompt, answer=None, lang=lang) for idx, prompt in enumerate(choices)]
            if self.none_option:
                self._choices.append(MCOption(0, prompt=self.none_prompt, lang=lang))

        elif all(isinstance(choice, MCOption) for choice in choices):
            self._choices = choices
        else:
            raise ValueError("Choices must be a list of strings or QuestionBool objects.")

    def set_answer(self, value=None):
        if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
            value = int(value)
            if value == 0:
                self.reset_answers()
                for choice in self._choices:
                    choice.set_answer(False)
                    if choice.idx == 0:
                        choice.set_answer(True)
                        self._answer.append(choice)
            else: # if answer is not 'None of the above'
                for choice in self._choices:
                    if choice.idx == value: # Append the choice to self._answer
                        choice.set_answer(True)
                        self._answer.append(choice)
                    elif choice.idx == 0 and value is not None: # Set 'None of the above' to False
                        choice.set_answer(False) 
                    else:
                        if self.mc_type == 'single-select': # Set all other choices to False if single-select
                            choice.set_answer(False)
        
    def set_prompt(self, value):
        self._prompt.update(value)

    @property
    def answer(self):
        if self.mc_type == 'single-select':
            return self._answer
        elif self.mc_type == 'multi-select':
            if len(self._answer) == 0:
                return []
            else:
                return self._answer
    
    def reset_answers(self):
        for choice in self.choices:
            choice.set_answer(None)
        self._answer = []

    def print_question(self, lang='sv'):
        print("")
        print(self.prompt.get(lang))
        for choice in self.choices:
            print(f"{choice.idx} - {choice.prompt.get(lang)}")

    def ask(self, lang='sv'):
        
        answer_lst = []
        
        if self.mc_type == 'single-select':
            while len(answer_lst) == 0:
                self.print_question(lang)
                raw_answer = input("Svar: ")
                answer_lst = raw_answer.split(",")
                if len(answer_lst) == 1:
                    try:
                        int_answer = int(answer_lst[0])
                        if int_answer in [opt.idx for opt in self.choices]:
                            self.set_answer(int_answer)
                            break
                    except:
                        pass
                print(f"Invalid answer: {raw_answer!r}, please try again.\n")
                answer_lst = []

        elif self.mc_type == 'multi-select':
            list_answer = [""]
            
            while not all(a.strip().isdigit() and int(a.strip()) in [c.idx for c in self.choices] for a in list_answer):
                self.reset_answers()
                self.print_question(lang)
                raw_answer = input("Svar: ")
                list_answer = raw_answer.split(",")    
                int_lst = [int(a.strip()) for a in list_answer]
            
            if any(i==0 for i in int_lst):
                self.set_answer(0)
            else:
                for i in int_lst:
                    self.set_answer(i)
            
        self.complete()

    def complete(self):
        self._answered = True
        if all(choice.answer == None for choice in self.choices):
            self.set_answer(0)
            return
        for choice in self.choices:
            if choice.answer is None:
                choice.set_answer(False)

    def __repr__(self):
        return f"MultipleChoice(prompt={self.prompt!r}, choices={self._choices!r})"