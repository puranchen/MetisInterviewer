from .question_abc import QuestionABC

class QuestionStr(QuestionABC):
    """ Question with a string answer. """
    def set_answer(self, value=None):
        if value is not None:
            self._answer = str(value)
            self._answered = True
    
    def ask(self, lang='en'):
        """ Ask the question to the user, default language is Swedish. Used for debugging and testing. """
        print("\n", self.prompt.get(lang), sep="")
        answer = input(self.INPUT_PROMPT[lang])
        self.set_answer(answer)
        self.asked = True

    def __repr__(self):
        return f"QuestionStr(prompt={self._prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionStr"]