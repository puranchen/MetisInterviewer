from abc import ABC, abstractmethod

class QuestionABC(ABC):
    """ Base class for all questions. """
    def __init__(self, prompt:str, answer=None, lang:str='en'):
        self._prompt = {lang: prompt}
        self._answer = None
        if answer is not None:
            self.set_answer(answer)

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

    def __repr__(self):
        return f"QuestionInt(prompt={self.prompt!r}, answer={self._answer!r})"
    
class QuestionFloat(QuestionABC):
    """ Question with a float answer. """
    def set_answer(self, value=None):
        if value is not None:
            if not isinstance(value, (float, int)):
                raise ValueError(f"Answer must be a float or int, got {type(value)}:")
            self._answer = float(value)
    
    def set_prompt(self, value):
        self._prompt.update(value)

    def __repr__(self):
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"
    
class QuestionStr(QuestionABC):
    """ Question with a string answer. """
    def set_answer(self, value=None):
        if value is not None:
            self._answer = str(value)
    
    def set_prompt(self, value):
        self._prompt.update(value)

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
    def __init__(self, prompt:str, choices:list, answer=None, lang:str='en', none_option=True, none_prompt="None of the above", mc_type='single-select', answered=False):
        super().__init__(prompt, answer, lang)
        self._choices = []
        self.none_option = none_option
        self.none_prompt = none_prompt
        self.mc_type = mc_type
        self._answered = False
        if answered:
            self.complete()
        self.set_choices(choices, lang)
        
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
        if isinstance(value, int):
            if value == 0:
                for choice in self._choices:
                    choice.set_answer(False)
                    if choice.idx == 0:
                        choice.set_answer(True)
            else:
                for choice in self._choices:
                    if choice.idx == value:
                        choice.set_answer(True)
                    elif choice.idx == 0:
                        choice.set_answer(False)
                    else:
                        if self.mc_type == 'single-select':
                            choice.set_answer(False)

    def set_prompt(self, value):
        self._prompt.update(value)

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