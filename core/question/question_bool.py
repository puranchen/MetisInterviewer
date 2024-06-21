from .question_abc import QuestionABC
from typing import Union

class QuestionBool(QuestionABC):
    """ Question with a boolean answer. """
    
    def __init__(self, prompt, **kwargs):
        super().__init__(prompt, **kwargs)
        self._answer = None

    def set_answer(self, value: Union[bool, int, None]) -> None:
        """ Set the answer to the question. """
        if not isinstance(value, (bool, type(None))) and value not in [0, 1]:
            raise ValueError(f"Answer must be a boolean or 0/1, got {type(value)}: {value}")
        self._answer = bool(value)

    def ask(self, lang: str = 'en') -> None:
        """ Ask the question to the user, default language is Swedish. Used for debugging and testing. """
        BOOLEAN_OPTIONS = {
            "sv": "1 - Ja\n2 - Nej", 
            "en": "1 - Yes\n2 - No"
        }
        while True:
            print("\n", self.prompt.get(lang), sep="")
            print(BOOLEAN_OPTIONS[lang])
            if self.skippable:
                print({'en': '0 - Skip question', 'sv': '0 - Hoppa över frågan'}[lang])
            answer = input(self.INPUT_PROMPT[lang]).strip()
            if self._is_valid_user_input(answer):
                if self.skippable and answer == "0":
                    self.asked = True
                    self._answer = None
                    break
                self.set_answer(answer == "1")
                self.asked = True
                break
            else:
                print("Invalid answer. Please try again.\n")

    def _is_valid_user_input(self, answer):
        """ Helper function to check if user input is a valid boolean. """
        if self.skippable:
            return answer in ["0", "1", "2"]
        else:
            return answer in ["1", "2"]
    
    def __repr__(self):
        return f"QuestionBool(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionBool"]