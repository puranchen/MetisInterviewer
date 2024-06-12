from .question_abc import QuestionABC
from typing import Union

class QuestionFloat(QuestionABC):
    """ Question with a float answer. """

    def __init__(self, prompt, unit, lang:str = 'en', min_value:float=None, max_value:float=None, skippable=False):
        super().__init__(prompt, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value

    def set_answer(self, value: Union[float, int]) -> None:
        """ Set the answer to the question. """
        if not isinstance(value, (float, int)):
            raise ValueError(f"Answer must be a float or int, got {type(value)}:")
        value = float(value) 
        if self.min_value and value < self.min_value:
            raise ValueError(f"Answer must be greater than {self.min_value}")
        if self.max_value and value > self.max_value:
            raise ValueError(f"Answer must be less than {self.max_value}")
        self._answer = value
    
    def ask(self, lang='sv') -> None:
        """ Ask the question to the user, default language is Swedish. """
        while True:
            print("\n", self.prompt.get(lang), sep="")
            response = input(f"{self.INPUT_PROMPT[lang]} ({self.unit}) ").replace(",",".")
            if self._is_valid_user_input(response):
                self.set_answer(float(response))
                self.asked = True
                break
            else:
                self._print_invalid_message(response)

    def _is_valid_user_input(self, response) -> bool:
        """ Helper function to check if user input is a valid integer. """
        try:
            value = float(response)
        except ValueError:
            return False
        if (self.max_value and value > self.max_value) or (self.min_value and value < self.min_value):
            return False
        return True
    
    def _print_invalid_message(self, response) -> None:
        """ Helper function to print an error message when user input is invalid. """
        if self.min_value is not None and self.max_value is not None:
            print(f"Invalid answer: {response!r}. Must be a number between {self.min_value!r} and {self.max_value!r}. Please try again.")
        elif self.min_value is not None:
            print(f"Invalid answer: {response!r}. Must be a number larger than {self.min_value!r}. Please try again.")
        elif self.max_value is not None:
            print(f"Invalid answer: {response!r}. Must be a number smaller than {self.max_value!r}. Please try again.")
        else:
            print(f"Invalid answer: {response!r}. Must be a number, please try again.")

    def __repr__(self):
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"
    
__all__ = ["QuestionFloat"]