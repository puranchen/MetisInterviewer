from . import QuestionABC

class QuestionBool(QuestionABC):
    """ Question with a boolean answer. """
    def set_answer(self, value: Union[bool, int,]):
        """ Set the answer to the question. """
        if not isinstance(value, (bool, type(None))) and value not in [0, 1]:
            raise ValueError(f"Answer must be a boolean or 0/1, got {type(value)}: {value}")
        self._answer = bool(value)

    def ask(self, lang='sv'):
        """ Used for debugging and testing, default language is Swedish """
        boolean_options = {
            "sv": "1 - Ja\n2 - Nej", 
            "en": "1 - Yes\n2 - No"
        }
        while True:
            print("\n", self.prompt.get(lang), sep="")
            print(boolean_options[lang])
            answer = input(self.INPUT_PROMPT[lang]).strip()
            if self._is_valid_user_input(answer):
                self.set_answer(answer == "1")
                self.asked = True
                break
            else:
                print("Invalid answer. Please try again.")

    def _is_valid_user_input(self, answer):
        """ Helper function to check if user input is a valid boolean. """
        return answer in ["1", "2"]
    
    def __repr__(self):
        return f"QuestionBool(prompt={self.prompt!r}, answer={self._answer!r})"