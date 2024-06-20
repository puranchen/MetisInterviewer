from question.question_float import QuestionFloat
import unittest
from unittest.mock import patch, MagicMock

class TestQuestionFloat(unittest.TestCase):

    def setUp(self):
        self.q = QuestionFloat(prompt="What did the thermometer show?", min_value=10, max_value=60)

    def test_question_float_init(self):
        self.assertFalse(self.q.asked)
        self.assertIsNone(self.q._answer)
        self.assertFalse(self.q.skippable)
        self.assertEqual(self.q.unit, None)
        self.assertEqual(self.q.min_value, 10.0)
        self.assertEqual(self.q.max_value, 60.0)

    def test_question_float_prompt_1(self):
        self.assertEqual(self.q.prompt, {'en': "What did the thermometer show?"})

    def test_question_float_prompt_2(self):
        self.q.set_prompt('Vad visade termometern?', 'sv')
        self.assertEqual(self.q.prompt, {'en': "What did the thermometer show?", 'sv': 'Vad visade termometern?'})

    def test_question_float_set_answer_valid(self):
        self.q.set_answer(38)
        self.assertEqual(self.q._answer, 38.0)

    def test_question_float_set_answer_invalid_type(self):
        with self.assertRaises(ValueError):
            self.q.set_answer("invalid")

    def test_question_float_set_answer_below_min(self):
        with self.assertRaises(ValueError):
            self.q.set_answer(5)

    def test_question_float_set_answer_above_max(self):
        with self.assertRaises(ValueError):
            self.q.set_answer(65)

    def test_question_float_is_valid_user_input(self):
        self.assertFalse(self.q._is_valid_user_input("a"))
        self.assertFalse(self.q._is_valid_user_input("38ºC"))
        self.assertFalse(self.q._is_valid_user_input("2"))
        self.assertTrue(self.q._is_valid_user_input("38.2"))
        self.assertTrue(self.q._is_valid_user_input("37.3"))
        self.assertFalse(self.q._is_valid_user_input("-30"))
        self.assertFalse(self.q._is_valid_user_input("60.1"))

    def test_question_float_print_invalid_message(self):
        with patch('builtins.print') as mocked_print:
            self.q._print_invalid_message("38ºC")
            mocked_print.assert_called_once_with("Invalid answer: '38ºC'. Must be a number between 10.0 and 60.0. Please try again.")

    @patch('builtins.input', side_effect=['15.5'])
    def test_question_float_ask(self, mock_input):
        with patch.object(self.q, '_print_invalid_message') as mock_print_invalid, \
                patch.object(self.q, '_is_valid_user_input', return_value=True):
            self.q.ask(lang='en')
            self.assertTrue(self.q.asked)
            self.assertEqual(self.q._answer, 15.5)
            mock_print_invalid.assert_not_called()

    @patch('builtins.input', side_effect=['invalid', '15.5'])
    def test_question_float_ask_invalid_then_valid(self, mock_input):
        with patch.object(self.q, '_print_invalid_message') as mock_print_invalid, \
                patch.object(self.q, '_is_valid_user_input', side_effect=[False, True]):
            self.q.ask(lang='en')
            self.assertTrue(self.q.asked)
            self.assertEqual(self.q._answer, 15.5)
            mock_print_invalid.assert_called_once()

    def test_question_float_repr(self):
        self.q.set_answer(38.0)
        expected_repr = "QuestionFloat(prompt={'en': 'What did the thermometer show?'}, answer=38.0None)"
        self.assertEqual(repr(self.q), expected_repr)

if __name__ == '__main__':
    unittest.main()
