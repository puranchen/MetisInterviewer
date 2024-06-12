from .question_abc import QuestionABC

class QuestionInt(QuestionABC):
    """ Question with an integer answer. """

    def __init__(self, prompt, unit, lang = 'en', min_value:int=None, max_value:int=None, skippable=False):
        super().__init__(prompt, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value

    def set_answer(self, value) -> None:
        """ Set the answer to the question. """
        if not isinstance(value, (int, type(None))):
            raise ValueError(f"Answer must be an integer or NoneType, got {type(value)}:")
        self._answer = value
        
    def ask(self, lang='sv') -> None:
        """ Ask the question to the user, default language is Swedish. Used for debugging and testing. """
        while True:
            # Print to console and get user input
            print("\n", self.prompt.get(lang), sep="")
            answer = input(f"{self.INPUT_PROMPT[lang]} ({self.unit}): ").replace(",",".")

            # Check if user input is valid
            if self._is_valid_user_input(answer):
                self.set_answer(int(answer))
                self.asked = True
                break
            else:
                self._print_invalid_message(answer)

    def _is_valid_user_input(self, answer: str) -> bool:
        """ Helper function to check if user input is a valid integer. """
        try:
            value = int(answer)
        except ValueError:
            return False
        
        if self.max_value and value > self.max_value:
            return False
        if self.min_value and value < self.min_value:
            return False
        
        return True
    
    def _print_invalid_message(self, answer) -> None:
        """ Helper function to print an error message when user input is invalid. """
        if self.min_value is not None and self.max_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number between {self.min_value!r} and {self.max_value!r}. Please try again.")
        elif self.min_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number larger than {self.min_value!r}. Please try again.")
        elif self.max_value is not None:
            print(f"Invalid answer: {answer!r}. Must be a number smaller than {self.max_value!r}. Please try again.")
        else:
            print(f"Invalid answer: {answer!r}. Must be a number, please try again.")

    def __repr__(self):
        return f"QuestionInt(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionInt"]