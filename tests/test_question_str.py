from question.question_str import QuestionStr
import unittest
from unittest.mock import patch

class TestQuestionStr(unittest.TestCase):

    def setUp(self):
        self.q = QuestionStr(prompt="What is your name?")

    def test_question_str_init(self):
        self.assertFalse(self.q.asked)
        self.assertFalse(self.q.skippable)
        self.assertEqual(self.q.prompt, {'en': "What is your name?"})

    def test_question_str_prompt_1(self):
        self.assertEqual(self.q.prompt, {'en': "What is your name?"})

    def test_question_str_prompt_2(self):
        self.q.set_prompt('Vad heter du?', 'sv')
        self.assertEqual(self.q.prompt, {'en': "What is your name?", 'sv': 'Vad heter du?'})

    def test_question_str_set_answer(self):
        self.q.set_answer("Alice")
        self.assertEqual(self.q._answer, "Alice")

    @patch('builtins.input', side_effect=['Alice'])
    def test_question_str_ask(self, mock_input):
        self.q.ask(lang='en')
        self.assertTrue(self.q.asked)
        self.assertEqual(self.q._answer, "Alice")

    def test_question_str_repr(self):
        self.q.set_answer("Alice")
        expected_repr = "QuestionStr(prompt={'en': 'What is your name?'}, answer='Alice')"
        self.assertEqual(repr(self.q), expected_repr)

if __name__ == '__main__':
    unittest.main()
