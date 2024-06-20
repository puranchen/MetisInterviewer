from .question_numerical import QuestionNumerical

class QuestionInt(QuestionNumerical):
    """ Question with an integer answer. """

    def __init__(self, prompt, **kwargs):
        super().__init__(prompt, value_type=int, **kwargs)

    def __repr__(self):
        return f"QuestionInt(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionInt"]