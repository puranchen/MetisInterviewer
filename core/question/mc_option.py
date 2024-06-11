from question_bool import QuestionBool

class MCOption(QuestionBool):
    """ Wrapper around QuestionBool for multiple choice options. """
    def __init__(self, idx, prompt:str, answer=None, lang:str='en'):
        super().__init__(prompt, answer, lang)
        self.idx = idx
    
    def __repr__(self):
        return f"MCOption(idx={self.idx!r}, prompt={self.prompt!r}, answer={self._answer!r})"

__all__ = ['MCOption']