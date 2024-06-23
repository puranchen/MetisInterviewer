from question.question_int import QuestionInt
import unittest
from unittest.mock import patch

class TestQuestionInt(unittest.TestCase):

    def setUp(self):
        self.q = QuestionInt(prompt="How many apples?", unit="pieces", min_value=1, max_value=10)

    def test_question_int_init(self):
        self.assertFalse(self.q.asked)
        self.assertFalse(self.q.skippable)
        self.assertEqual(self.q.unit, "pieces")
        self.assertEqual(self.q.min_value, 1)
        self.assertEqual(self.q.max_value, 10)

    def test_question_int_prompt_1(self):
        self.assertEqual(self.q.prompt, {'en': "How many apples?"})

    def test_question_int_prompt_2(self):
        self.q.set_prompt('Hur många äpplen?', 'sv')
        self.assertEqual(self.q.prompt, {'en': "How many apples?", 'sv': 'Hur många äpplen?'})

    def test_question_int_set_answer_valid(self):
        self.q.set_answer(5)
        self.assertEqual(self.q._answer, 5)

    def test_question_int_set_answer_invalid_type(self):
        with self.assertRaises(ValueError):
            self.q.set_answer("invalid")

    def test_question_int_set_answer_none(self):
        self.q.set_answer(None)
        self.assertIsNone(self.q._answer)

    def test_question_int_is_valid_user_input(self):
        self.assertFalse(self.q._is_valid_user_input("a"))
        self.assertFalse(self.q._is_valid_user_input("5.5"))
        self.assertFalse(self.q._is_valid_user_input("0"))
        self.assertTrue(self.q._is_valid_user_input("5"))
        self.assertFalse(self.q._is_valid_user_input("11"))

    def test_question_int_print_invalid_message(self):
        with patch('builtins.print') as mocked_print:
            self.q._print_invalid_message("5.5")
            mocked_print.assert_called_once_with("Invalid answer: '5.5'. Must be a number between 1 and 10. Please try again.")

    @patch('builtins.input', side_effect=['7'])
    def test_question_int_ask(self, mock_input):
        with patch.object(self.q, '_print_invalid_message') as mock_print_invalid, \
                patch.object(self.q, '_is_valid_user_input', return_value=True):
            self.q.ask(lang='en')
            self.assertTrue(self.q.asked)
            self.assertEqual(self.q._answer, 7)
            mock_print_invalid.assert_not_called()

    @patch('builtins.input', side_effect=['invalid', '7'])
    def test_question_int_ask_invalid_then_valid(self, mock_input):
        with patch.object(self.q, '_print_invalid_message') as mock_print_invalid, \
                patch.object(self.q, '_is_valid_user_input', side_effect=[False, True]):
            self.q.ask(lang='en')
            self.assertTrue(self.q.asked)
            self.assertEqual(self.q._answer, 7)
            mock_print_invalid.assert_called_once()

    def test_question_int_repr(self):
        self.q.set_answer(5)
        expected_repr = "QuestionInt(prompt={'en': 'How many apples?'}, answer=5)"
        self.assertEqual(repr(self.q), expected_repr)

if __name__ == '__main__':
    unittest.main()
