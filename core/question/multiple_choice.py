from .question_abc import QuestionABC
from .mc_option import MCOption

class MultipleChoice(QuestionABC):
    """ Question with multiple choice answers. """
    def __init__(self, prompt:str, choices:list, **kwargs):
        super().__init__(prompt, **kwargs)
        self._choices = []
        self.none_option = kwargs.get("none_option", False)
        self.none_prompt = kwargs.get("none_prompt", "None of the above")
        self.variant = kwargs.get("variant", 'single-select')
        self.answered = kwargs.get("answered", False)
        if self.answered:
            self.complete()
        self.set_choices(choices, kwargs.get('lang', 'en'), self.none_prompt)
        self._answer: list = []
        
    @property
    def choices(self):
        """ Get the choices for the question. """
        return self._choices
    
    def set_choices(self, choices:list, lang:str='en', none_prompt="None of the above"):
        """ Set the choices for the question. """
        # If the list of choices are strings, create MCOption objects from them
        if all(isinstance(choice, str) for choice in choices):
            self._choices = [MCOption(idx+1, prompt=prompt, answer=None, lang=lang) for idx, prompt in enumerate(choices)]
            if self.none_option:
                self._choices.append(MCOption(0, prompt=none_prompt, lang=lang))
        elif all(isinstance(choice, dict) for choice in choices):
            self._choices = [MCOption(idx+1, prompt=prompt, answer=None) for idx, prompt in enumerate(choices)]
            if self.none_option:
                self._choices.append(MCOption(0, prompt=none_prompt))
        # If the list of choices are MCOption objects, use them directly
        elif all(isinstance(choice, MCOption) for choice in choices):
            self._choices = choices
        else:
            raise ValueError("Choices must be a list of strings or MCOption objects.")

    def set_answer(self, value:int):
        """ Set the answer to the question using idx. """
        assert type(value) == int

        if value == 0:
            self.reset_answers()
            for choice in self._choices:
                choice.set_answer(False)
                if choice.idx == 0:
                    choice.set_answer(True)
                    self._answer.append(choice)
        else: # if answer is not 'None of the above'
            for choice in self._choices:
                if choice.idx == value: # Append the choice to self._answer
                    choice.set_answer(True)
                    self._answer.append(choice)
                elif choice.idx == 0 and value is not None: # Set 'None of the above' to False
                    choice.set_answer(False) 
                else:
                    if self.variant == 'single-select': # Set all other choices to False if single-select
                        choice.set_answer(False)
    
    def reset_answers(self):
        """ Reset the answer to the question. """
        for choice in self.choices:
            choice.set_answer(None)
        self._answer = []

    def print_question(self, lang):
        """ Print the question to the console. """
        print("\n", self.prompt.get(lang), sep="")
        for choice in self.choices:
            print(f"{choice.idx} - {choice.prompt.get(lang)}")

    def ask(self, lang='sv'):
        """ Used for debugging and testing """
        while True:
            self.reset_answers() # Reset answers when asking question
            self.print_question(lang)
            answer = input(self.INPUT_PROMPT[lang])

            if self.variant == 'single-select':
                if answer.isdigit():
                    int_answer = int(answer)
                    if int_answer in [opt.idx for opt in self.choices]:
                        self.set_answer(int_answer)
                        self.complete()
                        break
                print(f"Invalid answer: {answer!r}, please try again.\n")
                continue
            
            elif self.variant == 'multi-select':
                answer_lst = [a.strip() for a in answer.split(",")]
                if all(a.isdigit() for a in answer_lst):
                    if all(int(a) in [c.idx for c in self.choices] for a in answer_lst):
                        answer_lst = [int(a) for a in answer_lst]
                        if any(i==0 for i in answer_lst):
                            self.set_answer(0)
                        else:
                            for i in answer_lst:
                                self.set_answer(i)
                        self.complete()
                        break
                print(f"Invalid answer: {answer!r}, please try again.\n")
                continue

    def complete(self):
        """ Assign unassigned questions among multiple choices """
        if all(choice.answer == None for choice in self.choices):
            self.set_answer(0)
            return
        for choice in self.choices:
            if choice.answer is None:
                choice.set_answer(False)
        self.asked = True

    def __repr__(self):
        return f"MultipleChoice(prompt={self.prompt!r}, choices={self._choices!r})"
    
__all__ = ['MultipleChoice']