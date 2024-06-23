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
        self._answer = None
        self.prompt = (prompt, kwargs.get("lang", "en"))
        self.skippable = kwargs.get("skippable", False)
        self.asked = False
        if kwargs.get("answer", None) is not None:
            self.set_answer(kwargs.get("answer"))
        if isinstance(prompt, str):
            self.lang = kwargs.get("lang", "en")
        elif isinstance(prompt, dict):
            self.lang = list(prompt.keys())[0]
    
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