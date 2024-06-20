import unittest
from question.question_abc import QuestionABC
from typing import Dict

# Concrete subclass for testing
class TestQuestion(QuestionABC):
    def set_answer(self, value):
        self._answer = value

class TestQuestionABC(unittest.TestCase):

    def setUp(self):
        self.q = TestQuestion(prompt="What is the capital of France?", lang='en')

    def test_question_abc_init(self):
        self.assertEqual(self.q.prompt, {'en': "What is the capital of France?"})
        self.assertFalse(self.q.asked)
        self.assertFalse(self.q.skippable)
        self.assertIsNone(self.q.answer)

    def test_question_abc_set_prompt_valid(self):
        self.q.set_prompt('Vad är huvudstaden i Frankrike?', 'sv')
        self.assertEqual(self.q.prompt, {'en': "What is the capital of France?", 'sv': 'Vad är huvudstaden i Frankrike?'})

    def test_question_abc_set_prompt_invalid_language(self):
        with self.assertRaises(ValueError):
            self.q.set_prompt('What is the capital of France?', 'de')

    def test_question_abc_set_answer(self):
        self.q.set_answer('Paris')
        self.assertEqual(self.q.answer, 'Paris')

    def test_question_abc_input_prompt(self):
        self.assertEqual(self.q.INPUT_PROMPT, {"sv": "Svar: ", "en": "Answer: "})

if __name__ == '__main__':
    unittest.main()
