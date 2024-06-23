import unittest
from question.multiple_choice import MultipleChoice
from question.mc_option import MCOption
from unittest.mock import patch

class TestMultipleChoice(unittest.TestCase):

    def setUp(self):
        self.q = MultipleChoice(
            prompt="What is your favorite color?",
            choices=["Red", "Blue", "Green"],
            lang='en',
            none_option=True,
            none_prompt="None of the above",
            variant='single-select'
        )

    def test_multiple_choice_init(self):
        self.assertEqual(self.q.prompt, {'en': "What is your favorite color?"})
        self.assertFalse(self.q.asked)
        self.assertFalse(self.q.skippable)
        self.assertEqual(len(self.q.choices), 4)  # Includes None of the above option
        self.assertEqual(self.q.choices[-1].prompt['en'], "None of the above")

    def test_multiple_choice_set_choices_with_strings(self):
        choices = ["Purple", "Amber", "Orange", "Yellow"]
        self.q.set_choices(choices, lang='en', none_prompt="None of the above")
        self.assertEqual(len(self.q.choices), 5)
        self.assertTrue(all(isinstance(choice, MCOption) for choice in self.q.choices))

    def test_multiple_choice_set_choices_with_mcoptions(self):
        choices = [MCOption(1, prompt="Red"), MCOption(2, prompt="Blue"), MCOption(3, prompt="Green")]
        self.q.set_choices(choices, lang='en')
        self.assertEqual(len(self.q.choices), 3)
        self.assertTrue(all(isinstance(choice, MCOption) for choice in self.q.choices))

    def test_multiple_choice_set_choices_invalid(self):
        choices = ["Red", 1, "Green"]
        with self.assertRaises(ValueError):
            self.q.set_choices(choices, lang='en')

    def test_multiple_choice_set_answer_single_select(self):
        self.q.set_answer(1)
        self.assertTrue(self.q.choices[0].answer)
        self.assertFalse(self.q.choices[1].answer)
        self.assertFalse(self.q.choices[2].answer)
        self.assertFalse(self.q.choices[3].answer)

    def test_multiple_choice_set_answer_none_option(self):
        self.q.set_answer(0)
        self.assertTrue(self.q.choices[-1].answer)
        self.assertFalse(self.q.choices[0].answer)
        self.assertFalse(self.q.choices[1].answer)
        self.assertFalse(self.q.choices[2].answer)

    def test_multiple_choice_reset_answers(self):
        self.q.set_answer(1)
        self.q.reset_answers()
        for choice in self.q.choices:
            self.assertFalse(choice.answer)
        self.assertEqual(self.q._answer, [])

    @patch('builtins.input', side_effect=['1'])
    def test_multiple_choice_ask_single_select(self, mock_input):
        with patch.object(self.q, 'print_question') as mock_print_question, \
                patch.object(self.q, 'reset_answers') as mock_reset_answers:
            self.q.ask(lang='en')
            self.assertTrue(self.q.asked)
            self.assertEqual(self.q._answer, [self.q.choices[0]])
            mock_print_question.assert_called()
            mock_reset_answers.assert_called()

    @patch('builtins.input', side_effect=['1,2'])
    def test_multiple_choice_ask_multi_select(self, mock_input):
        self.q.variant = 'multi-select'
        with patch.object(self.q, 'print_question') as mock_print_question, \
                patch.object(self.q, 'reset_answers') as mock_reset_answers:
            self.q.ask(lang='en')
            self.assertTrue(self.q.asked)
            self.assertEqual(self.q._answer, [self.q.choices[0], self.q.choices[1]])
            mock_print_question.assert_called()
            mock_reset_answers.assert_called()

    def test_multiple_choice_repr(self):
        expected_repr = f"MultipleChoice(prompt={{'en': 'What is your favorite color?'}}, choices={self.q.choices!r})"
        self.assertEqual(repr(self.q), expected_repr)

if __name__ == '__main__':
    unittest.main()
