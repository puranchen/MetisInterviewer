from abc import ABC, abstractmethod
from typing import Dict, Union

SUPPORTED_LANGUAGES = ["sv", "en"]

class QuestionABC(ABC):
    """Base class for all questions."""
    
    INPUT_PROMPT: Dict[str, str] = {
        "sv": "Svar: ",
        "en": "Answer: "
    }

    def __init__(self, prompt, **kwargs):
        self._prompt = {}
        self._skippable:bool = False
        self._asked:bool = False
        self._answered:bool = False
        self._answer = None

        self.prompt = (prompt, kwargs.get("lang", "en"))
        self.skippable = kwargs.get("skippable", False)
        self.asked = kwargs.get("asked", False)

        answer_input = kwargs.get("answer", None)
        if answer_input is not None:
            self.set_answer(answer_input)
    
    @property
    def prompt(self):
        """ Get the prompt for the question. """
        return self._prompt

    @prompt.setter
    def prompt(self, value):
        prompt, lang = value
        if isinstance(prompt, str):
            self._prompt = {lang: prompt}
        elif isinstance(prompt, dict):            
            self._prompt = prompt
        else:
            raise ValueError("Prompt must be a string or a dictionary with a language key.")

    @property
    def skippable(self):
        return self._skippable
    
    @skippable.setter
    def skippable(self, value):
        assert isinstance(value, bool)
        self._skippable = value

    @property
    def asked(self):
        return self._asked
    
    @asked.setter
    def asked(self, value):
        assert isinstance(value, bool)
        self._asked = value

    @property
    def answered(self):
        return self._answered

    @answered.setter
    def answered(self, value):
        assert isinstance(value, bool)
        self._answered = value

    @property
    def answer(self):
        """ Get the answer to the question. """
        return self._answer
    
    def set_prompt(self, prompt, lang='en') -> None:
        """Adds prompt in the specified language. Mainly used for multi-lingual support."""
        if lang not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {lang}. Supported languages are: {SUPPORTED_LANGUAGES}")
        self._prompt.update({lang: prompt})
    
    @abstractmethod
    def set_answer(self, value):
        """ Set the answer to the question. """
        pass
    
    

__all__ = ['QuestionABC']