from question.question_bool import QuestionBool
import unittest
from unittest.mock import patch

class TestQuestionBool(unittest.TestCase):

    def setUp(self):
        self.q = QuestionBool("Is the sky blue?")
        self.assertFalse(self.q.asked)
        self.assertFalse(self.q.answered)

    def test_question_bool_init(self):
        self.assertFalse(self.q.asked)
        self.assertIsNone(self.q._answer)
        self.assertFalse(self.q.skippable)

    def test_question_bool_prompt_1(self):
        self.assertTrue(self.q.prompt == {'en': "Is the sky blue?"})
    
    def test_question_bool_prompt_2(self):
        self.q.set_prompt('Är himlen blå?', 'sv')    
        self.assertTrue(self.q.prompt == {'en': "Is the sky blue?", 'sv': 'Är himlen blå?'})

    def test_question_bool_set_answer_1(self):
        self.q.set_answer(True)
        self.assertTrue(self.q.answer)
        self.q.set_answer(False)
        self.assertFalse(self.q.answer)
        self.assertTrue(self.q.answered)

    def test_question_bool_set_answer_2(self):
        self.q.set_answer(1)
        self.assertTrue(self.q.answer)
        self.q.set_answer(0)
        self.assertFalse(self.q.answer)
        self.assertFalse(self.q.answer)
        self.assertTrue(self.q.answered)

    def test_question_bool_is_invalid_answer(self):
        self.assertFalse(self.q._is_valid_user_input("3"))
        self.assertTrue(self.q._is_valid_user_input("1"))
        self.assertTrue(self.q._is_valid_user_input("2"))
        self.assertFalse(self.q._is_valid_user_input("0"))

    @patch('builtins.input', return_value='1')
    def test_question_bool_ask_valid_input(self, mock_input):
        self.q.ask()
        self.assertTrue(self.q.asked)
        self.assertTrue(self.q.answered)

    @patch('builtins.input', side_effect=['3', '1'])
    @patch('builtins.print')
    def test_question_bool_ask_invalid_input_then_valid(self, mock_print, mock_input):
        self.q.ask()
        self.assertTrue(self.q.asked)
        mock_print.assert_any_call("Invalid answer. Please try again.\n")


if __name__ == '__main__':
    unittest.main()