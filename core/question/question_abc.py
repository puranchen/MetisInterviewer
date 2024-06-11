from abc import ABC, abstractmethod
from typing import Dict

SUPPORTED_LANGUAGES = ["sv", "en"]



class QuestionABC(ABC):
    """Base class for all questions."""
    
    INPUT_PROMPT: Dict[str, str] = {
        "sv": "Svar: ",
        "en": "Answer: "
    }

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

__all__ = ['QuestionABC']