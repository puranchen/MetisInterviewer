from abc import ABC, abstractmethod
from typing import Union

input_prompt = {
    "sv": "Svar: ",
    "en": "Answer: "
}

SUPPORTED_LANGUAGES = ["sv", "en"]

class QuestionABC(ABC):
    """ Base class for all questions. """
    def __init__(self, prompt:str, answer=None, lang:str='en', skippable=False, asked=False):
        self._prompt = {lang: prompt}
        self._answer = None
        self.skippable = skippable
        self.asked = asked
        if answer is not None:
            self.set_answer(answer)

    @property
    def prompt(self):
        """ Get the prompt for the question. """
        return self._prompt

    @property
    def answer(self):
        """ Get the answer to the question. """
        return self._answer
    
    def set_prompt(self, prompt, lang):
        """Sets the prompt in the specified language."""
        if lang not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {lang}")
        self._prompt.update({lang: prompt})
    
    @abstractmethod
    def set_answer(self, value):
        """ Set the answer to the question. """
        pass
    
class QuestionBool(QuestionABC):
    """ Question with a boolean answer. """
    def set_answer(self, value: Union[bool, int,]):
        """ Set the answer to the question. """
        if not isinstance(value, (bool, type(None))) and value not in [0, 1]:
            raise ValueError(f"Answer must be a boolean or 0/1, got {type(value)}: {value}")
        self._answer = bool(value)

    def ask(self, lang='sv'):
        """ Used for debugging and testing, default language is Swedish """
        boolean_options = {
            "sv": "1 - Ja\n2 - Nej", 
            "en": "1 - Yes\n2 - No"
        }
        while True:
            print("\n", self.prompt.get(lang), sep="")
            print(boolean_options[lang])
            answer = input(input_prompt[lang]).strip()
            if self._is_valid_user_input(answer):
                self.set_answer(answer == "1")
                self.asked = True
                break
            else:
                print("Invalid answer. Please try again.")

    def _is_valid_user_input(self, answer):
        """ Helper function to check if user input is a valid boolean. """
        return answer in ["1", "2"]
    
    def __repr__(self):
        return f"QuestionBool(prompt={self.prompt!r}, answer={self._answer!r})"

class QuestionInt(QuestionABC):
    """ Question with an integer answer. """

    def __init__(self, prompt, lang = 'en', min_value:int=None, max_value:int=None):
        super().__init__(prompt, lang=lang)
        self.max_value = max_value
        self.min_value = min_value

    def set_answer(self, value):
        """ Set the answer to the question. """
        if not isinstance(value, (int, type(None))):
            raise ValueError(f"Answer must be an integer or NoneType, got {type(value)}:")
        self._answer = value
        
    def ask(self, lang='sv'):
        """ used for debugging and testing """
        while True:
            # Print to console and get user input
            print("\n", self.prompt.get(lang), sep="")
            answer = input(f"{input_prompt[lang]} ({self.unit}): ").replace(",",".")

            # Check if user input is valid
            if self._is_valid_user_input(answer):
                self.set_answer(int(answer))
                self.asked = True
                break
            else:
                self._print_invalid_message(answer)

    def _is_valid_user_input(self, answer):
        """ Helper function to check if user input is a valid integer. """
        try:
            value = int(answer)
        except ValueError:
            return False
        
        if self.max_value and value > self.max_value:
            return False
        if self.min_value and value < self.min_value:
            return False
        
        return True
    
    def _print_invalid_message(self, answer):
        """ Helper function to print an error message when user input is invalid. """
        if self.min_value is not None and self.max_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number between {self.min_value!r} and {self.max_value!r}. Please try again.")
        elif self.min_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number larger than {self.min_value!r}. Please try again.")
        elif self.max_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number smaller than {self.max_value!r}. Please try again.")
        else:
            print(f"Invalid answer: {answer!r}. Must be a number, please try again.")

    def __repr__(self):
        return f"QuestionInt(prompt={self.prompt!r}, answer={self._answer!r})"
    
class QuestionFloat(QuestionABC):
    """ Question with a float answer. """
    def __init__(self, prompt, unit, lang = 'en', min_value:float=None, max_value:float=None, skippable=False):
        super().__init__(prompt, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value

    def set_answer(self, value: Union[float, int]):
        """ Set the answer to the question. """
        if not isinstance(value, (float, int)): # Accept floats and ints (typecasts to float)
            raise ValueError(f"Answer must be a float or int, got {type(value)}:")
        else: # Check if value within boundaries when applicable
            if self.min_value and value < self.min_value:
                raise ValueError(f"Answer must be greater than {self.min_value}")
            if self.max_value and value > self.max_value:
                raise ValueError(f"Answer must be less than {self.max_value}")
        self._answer = float(value) 
    
    def ask(self, lang='sv'):
        """ Used for debugging and testing """
        while True:
            # Print to console and get user input
            print("\n", self.prompt.get(lang), sep="")
            answer = input(f"{input_prompt[lang]} ({self.unit}) ").replace(",",".")

            # Check if user input is valid
            if self._is_valid_user_input(answer):
                self.set_answer(float(answer))
                self.asked = True
                break
            else:
                self._print_invalid_message(answer)

    def _is_valid_user_input(self, answer):
        """ Helper function to check if user input is a valid integer. """
        try:
            value = float(answer)
        except ValueError:
            return False
        
        if self.max_value and value > self.max_value:
            return False
        if self.min_value and value < self.min_value:
            return False
        
        return True
    
    def _print_invalid_message(self, answer):
        """ Helper function to print an error message when user input is invalid. """
        if self.min_value is not None and self.max_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number between {self.min_value!r} and {self.max_value!r}. Please try again.")
        elif self.min_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number larger than {self.min_value!r}. Please try again.")
        elif self.max_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number smaller than {self.max_value!r}. Please try again.")
        else:
            print(f"Invalid answer: {answer!r}. Must be a number, please try again.")

    def __repr__(self):
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"
    
class QuestionStr(QuestionABC):
    """ Question with a string answer. """
    def set_answer(self, value=None):
        if value is not None:
            self._answer = str(value)
    
    def ask(self, lang='sv'):
        """ Used for debugging and testing """
        print("\n", self.prompt.get(lang), sep="")
        answer = input(input_prompt[lang])
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
    def __init__(self, prompt:str, choices:list, answer:list=None, lang:str='en', none_option=True, none_prompt="None of the above", variant='single-select', answered=False):
        super().__init__(prompt, answer, lang)
        self._choices = []
        self.none_option = none_option
        self.variant = variant
        if answered:
            self.complete()
        self.set_choices(choices, lang, none_prompt)
        self._answer: list = []
        
    @property
    def choices(self):
        """ Get the choices for the question. """
        return self._choices
    
    def set_choices(self, choices:list, lang:str='en', none_prompt="None of the above"):
        if all(isinstance(choice, str) for choice in choices):
            self._choices = [MCOption(idx+1, prompt=prompt, answer=None, lang=lang) for idx, prompt in enumerate(choices)]
            if self.none_option:
                self._choices.append(MCOption(0, prompt=none_prompt, lang=lang))

        elif all(isinstance(choice, MCOption) for choice in choices):
            self._choices = choices
        else:
            raise ValueError("Choices must be a list of strings or QuestionBool objects.")

    def set_answer(self, value:int):
        """ Set the answer to the question. """
        assert type(value) == int

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
                    if self.variant == 'single-select': # Set all other choices to False if single-select
                        choice.set_answer(False)
    
    def reset_answers(self):
        """ Reset the answer to the question. """
        for choice in self.choices:
            choice.set_answer(None)
        self._answer = []

    def print_question(self, lang):
        """ Print the question to the console. """
        print("\n", self.prompt.get(lang), sep="")
        for choice in self.choices:
            print(f"{choice.idx} - {choice.prompt.get(lang)}")

    def ask(self, lang='sv'):
        """ Used for debugging and testing """
        while True:
            self.reset_answers() # Rest answers when asking question
            self.print_question(lang)
            answer = input(input_prompt[lang])

            if self.variant == 'single-select':
                if answer.isdigit():
                    int_answer = int(answer)
                    if int_answer in [opt.idx for opt in self.choices]:
                        self.set_answer(int_answer)
                        self.complete()
                        break
                print(f"Invalid answer: {answer!r}, please try again.\n")
                continue
            
            elif self.variant == 'multi-select':
                answer_lst = [a.strip() for a in answer.split(",")]
                if all(a.isdigit() for a in answer_lst):
                    if all(int(a) in [c.idx for c in self.choices] for a in answer_lst):
                        answer_lst = [int(a) for a in answer_lst]
                        if any(i==0 for i in answer_lst):
                            self.set_answer(0)
                        else:
                            for i in answer_lst:
                                self.set_answer(i)
                        self.complete()
                        break
                print(f"Invalid answer: {answer!r}, please try again.\n")
                continue

    def complete(self):
        """ Assign unassigned questions among multiple choices """
        if all(choice.answer == None for choice in self.choices):
            self.set_answer(0)
            return
        for choice in self.choices:
            if choice.answer is None:
                choice.set_answer(False)
        self.asked = True

    def __repr__(self):
        return f"MultipleChoice(prompt={self.prompt!r}, choices={self._choices!r})"
