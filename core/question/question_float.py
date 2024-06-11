from . import QuestionABC
from typing import Union

class QuestionFloat(QuestionABC):
    """ Question with a float answer. """
    def __init__(self, prompt, unit, lang = 'en', min_value:float=None, max_value:float=None, skippable=False):
        super().__init__(prompt, lang=lang, skippable=skippable)
        self.unit = unit
        self.max_value = max_value
        self.min_value = min_value

    def set_answer(self, value: Union[float, int]):
        """ Set the answer to the question. """
        if not isinstance(value, (float, int)): # Accept floats and ints (typecasts to float)
            raise ValueError(f"Answer must be a float or int, got {type(value)}:")
        else: # Check if value within boundaries when applicable
            if self.min_value and value < self.min_value:
                raise ValueError(f"Answer must be greater than {self.min_value}")
            if self.max_value and value > self.max_value:
                raise ValueError(f"Answer must be less than {self.max_value}")
        self._answer = float(value) 
    
    def ask(self, lang='sv'):
        """ Used for debugging and testing """
        while True:
            # Print to console and get user input
            print("\n", self.prompt.get(lang), sep="")
            answer = input(f"{self.INPUT_PROMPT[lang]} ({self.unit}) ").replace(",",".")

            # Check if user input is valid
            if self._is_valid_user_input(answer):
                self.set_answer(float(answer))
                self.asked = True
                break
            else:
                self._print_invalid_message(answer)

    def _is_valid_user_input(self, answer):
        """ Helper function to check if user input is a valid integer. """
        try:
            value = float(answer)
        except ValueError:
            return False
        
        if self.max_value and value > self.max_value:
            return False
        if self.min_value and value < self.min_value:
            return False
        
        return True
    
    def _print_invalid_message(self, answer):
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
        return f"QuestionFloat(prompt={self.prompt!r}, answer={self._answer!r})"