import unittest
from question.question_abc import QuestionABC
from typing import Dict

class DummyQuestion(QuestionABC):
    """Dummy implementation of QuestionABC for testing purposes."""
    
    def __init__(self, prompt, **kwargs):
        super().__init__(prompt, **kwargs)
        self._answer = None  # Initialize _answer attribute
    
    def set_answer(self, value):
        self._answer = value

class TestQuestionABC(unittest.TestCase):

    def test_initialization(self):
        """Test that a QuestionABC object is initialized correctly."""
        question = DummyQuestion("Is this a test?")
        self.assertEqual(question.prompt.get("en"), "Is this a test?")
        self.assertIsNone(question.answer)
        self.assertFalse(question.asked)
        self.assertFalse(question.skippable)
    
    def test_initialization_with_kwargs(self):
        """Test that a QuestionABC object is initialized correctly with additional kwargs."""
        question = DummyQuestion("Is this a test?", skippable=True, lang="en", answer="Yes")
        self.assertEqual(question.prompt.get("en"), "Is this a test?")
        self.assertFalse(question.asked)
        self.assertTrue(question.skippable)
    
    def test_set_prompt(self):
        """Test that the set_prompt method works correctly for different languages."""
        question = DummyQuestion("Is this a test?")
        question.set_prompt("Är detta ett test?", "sv")
        self.assertEqual(question.prompt.get("sv"), "Är detta ett test?")
        self.assertEqual(question.prompt.get("en"), "Is this a test?")
    
    def test_set_prompt_invalid_language(self):
        """Test that the set_prompt method raises an error for unsupported languages."""
        question = DummyQuestion("Is this a test?")
        with self.assertRaises(ValueError):
            question.set_prompt("C'est un test?", "fr")
    
    def test_set_answer(self):
        """Test that the set_answer method in the subclass works correctly."""
        question = DummyQuestion("Is this a test?")
        question.set_answer("Yes")
        self.assertEqual(question.answer, "Yes")
    
    def test_input_prompt(self):
        """Test that the input prompt dictionary is correct."""
        self.assertEqual(DummyQuestion.INPUT_PROMPT["sv"], "Svar: ")
        self.assertEqual(DummyQuestion.INPUT_PROMPT["en"], "Answer: ")

if __name__ == "__main__":
    unittest.main()
