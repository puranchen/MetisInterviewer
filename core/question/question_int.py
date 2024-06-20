from .question_abc import QuestionABC
from .question_numerical import QuestionNumerical

class QuestionInt(QuestionNumerical):
    """ Question with an integer answer. """

    def __init__(self, prompt, unit=None, lang = 'en', min_value:int=None, max_value:int=None, skippable=False):
        super().__init__(prompt, value_type=int, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value

    def __repr__(self):
        return f"QuestionInt(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionInt"]