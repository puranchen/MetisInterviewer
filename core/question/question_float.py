from .question_numerical import QuestionNumerical

class QuestionFloat(QuestionNumerical):
    """ Question with a float answer. """

    def __init__(self, prompt, **kwargs):
        super().__init__(prompt, value_type=float, **kwargs)
    
    def __repr__(self):
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionFloat"]