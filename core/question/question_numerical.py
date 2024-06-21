from .question_abc import QuestionABC
from abc import abstractmethod

class QuestionNumerical(QuestionABC):
    """ Question with a numerical answer. """

    def __init__(self, prompt, **kwargs):
        super().__init__(prompt, **kwargs)
        self.unit = kwargs.get("unit", None)
        self.value_type = kwargs.get("value_type")
        self.max_value = kwargs.get("max_value", None)
        self.min_value = kwargs.get("min_value", None)

    @property
    def max_value(self):
        return self._max_value
    
    @max_value.setter
    def max_value(self, value):
        # max_value must be in integer if value_type is int
        if isinstance(value, float) and self.value_type == int:
            raise ValueError(f"max_value must be an integer if value_type is int, got {type(value)}")

        if value is not None:
            if self.value_type == float: #always typecast to float if value_type is float
                self._max_value = float(value)
            
            else:
                self._max_value = self.value_type(value)
        else:   
            self._max_value = None

    @property
    def min_value(self):
        return self._min_value
    
    @min_value.setter
    def min_value(self, value):
        if value is not None:
            if self.value_type == float:
                self._min_value = float(value)
            elif isinstance(value, float) and self.value_type == int:
                raise ValueError(f"min_value must be an integer if value_type is int, got {type(value)}")
            else:
                self._min_value = self.value_type(value)
        else:
            self._min_value = None

    def set_answer(self, value) -> None:
        if not isinstance(value, (self.value_type, type(None))):
            raise ValueError(f"Answer must be a {self.value_type} or NoneType, got {type(value)}:")
        if isinstance(value, self.value_type):
            if self._min_value is not None and self._min_value > value:
                raise ValueError(f"Answer must be greater than {self.min_value}")
            if self._max_value is not None and value > self._max_value:
                raise ValueError(f"Answer must be less than {self.max_value}")
        self._answer = value

    def ask(self, lang='en') -> None:
        while True:
            print("\n", self._prompt.get(lang), sep="")
            if self.skippable:
                print({'en': 'Enter `-` to skip', 'sv': 'Svara `-` för att hoppa över'}[lang])
            response = input(f"{self.INPUT_PROMPT[lang]} ({self.unit}) ").replace(",",".")
            if self._is_valid_user_input(response):
                if response == "-":
                    self.asked = True
                    self.set_answer(None)
                    break
                self.set_answer(self.value_type(response))
                self.asked = True
                break
            else:
                self._print_invalid_message(response)

    def _is_valid_user_input(self, response) -> bool:
        if self.skippable and response == "-":
            return True
        try:
            value = self.value_type(response)
        except ValueError:
            return False
        if (self.max_value and value > self.max_value) or (self.min_value and value < self.min_value):
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