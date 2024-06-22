from abc import ABC, abstractmethod
from typing import Dict

SUPPORTED_LANGUAGES = ["sv", "en"]

class QuestionABC(ABC):
    """Base class for all questions."""
    
    INPUT_PROMPT: Dict[str, str] = {
        "sv": "Svar: ",
        "en": "Answer: "
    }

    def __init__(self, prompt, **kwargs):
        if isinstance(prompt, str):
            self._prompt = {kwargs.get("lang", 'en'): prompt}
        elif isinstance(prompt, dict): 
            key_list = list(prompt)
            assert all(v in SUPPORTED_LANGUAGES for v in key_list), f"Supported languages are: {SUPPORTED_LANGUAGES}"
            self._prompt = prompt
        self.skippable = kwargs.get("skippable", False)
        self.asked = False
        if kwargs.get("answer", None) is not None:
            self.set_answer(kwargs.get("answer"))
        self._answer = None
    
    @property
    def prompt(self):
        """ Get the prompt for the question. """
        return self._prompt

    @property
    def answer(self):
        """ Get the answer to the question. """
        return self._answer
    
    def set_prompt(self, prompt, lang) -> None:
        """Sets prompt in the specified language. Mainly used for multi-lingual support."""
        if lang not in SUPPORTED_LANGUAGES:
            raise ValueError(f"Unsupported language: {lang}. Supported languages are: {SUPPORTED_LANGUAGES}")
        self._prompt.update({lang: prompt})
    
    @abstractmethod
    def set_answer(self, value):
        """ Set the answer to the question. """
        pass

__all__ = ['QuestionABC']