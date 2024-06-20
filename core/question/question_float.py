from typing import Union
from .question_numerical import QuestionNumerical

class QuestionFloat(QuestionNumerical):
    """ Question with a float answer. """

    def __init__(self, prompt, unit=None, lang:str = 'en', min_value:float=None, max_value:float=None, skippable=False):
        super().__init__(prompt, value_type=float, unit=unit, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value
    
__all__ = ["QuestionFloat"]