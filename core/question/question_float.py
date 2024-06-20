from typing import Union
from .question_numerical import QuestionNumerical

class QuestionFloat(QuestionNumerical):
    """ Question with a float answer. """

    def __init__(self, prompt, unit=None, lang:str = 'en', min_value:float=None, max_value:float=None, skippable=False):
        super().__init__(prompt, value_type=float, unit=unit, lang=lang, skippable=skippable)
    
    def __repr__(self):
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionFloat"]