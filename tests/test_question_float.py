from question.question_float import QuestionFloat
import unittest
from unittest.mock import patch, MagicMock

class TestQuestionFloat(unittest.TestCase):

    def test_initialization(self):
        """Test that a QuestionFloat object is initialized correctly."""
        question = QuestionFloat("What is the temperature?")
        self.assertEqual(question.prompt.get("en"), "What is the temperature?")
        self.assertFalse(question.asked)
        self.assertFalse(question.skippable)
        self.assertEqual(question.value_type, float)
        self.assertIsNone(question.max_value)
        self.assertIsNone(question.min_value)
        self.assertIsNone(question.unit)
        with self.assertRaises(ValueError):
            question.set_answer("a")
        with self.assertRaises(ValueError):
            question.set_answer(0)

    def test_initialization_with_kwargs(self):
        """Test that a QuestionFloat object is initialized correctly with additional kwargs."""
        question = QuestionFloat("What is the temperature?", skippable=True, lang="en", unit="C", min_value=0.0, max_value=100.0)
        self.assertEqual(question.prompt.get("en"), "What is the temperature?")
        self.assertFalse(question.asked)
        self.assertTrue(question.skippable)
        self.assertEqual(question.unit, "C")
        self.assertEqual(question.min_value, 0.0)
        self.assertEqual(question.max_value, 100.0)
        with self.assertRaises(ValueError):
            question.set_answer(-1.0)
        with self.assertRaises(ValueError):
            question.set_answer(101.0)

    def test_set_answer(self):
        """Test that the set_answer method works correctly."""
        question = QuestionFloat("What is the temperature?", min_value=0.0, max_value=100.0)
        question.set_answer(25.5)
        self.assertEqual(question.answer, 25.5)
    
    def test_set_answer_invalid(self):
        """Test that the set_answer method raises an error with invalid inputs."""
        question = QuestionFloat("What is the temperature?", min_value=0.0, max_value=100.0)
        with self.assertRaises(ValueError):
            question.set_answer("Invalid")
    
    def test_set_prompt(self):
        """Test that the set_prompt method works correctly for different languages."""
        question = QuestionFloat("What is the temperature?")
        question.set_prompt("Vad är temperaturen?", "sv")
        self.assertEqual(question.prompt.get("sv"), "Vad är temperaturen?")
        self.assertEqual(question.prompt.get("en"), "What is the temperature?")
    
    def test_set_prompt_invalid_language(self):
        """Test that the set_prompt method raises an error for unsupported languages."""
        question = QuestionFloat("What is the temperature?")
        with self.assertRaises(ValueError):
            question.set_prompt("Quelle est la température?", "fr")
    
    def test_max_value_setter(self):
        """Test that the max_value setter works correctly."""
        question = QuestionFloat("What is the temperature?", max_value=100.0)
        self.assertEqual(question.max_value, 100.0)
    
    def test_min_value_setter(self):
        """Test that the min_value setter works correctly."""
        question = QuestionFloat("What is the temperature?", min_value=0.0)
        self.assertEqual(question.min_value, 0.0)
 
if __name__ == "__main__":
    unittest.main()