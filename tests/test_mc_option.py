import unittest
from question.mc_option import MCOption
import unittest

class TestMCOption(unittest.TestCase):

    def test_initialization(self):
        """Test that an MCOption object is initialized correctly."""
        option = MCOption(1, "Is this a test?")
        self.assertEqual(option.idx, 1)
        self.assertEqual(option.prompt.get("en"), "Is this a test?")
        self.assertIsNone(option.answer)
    
    def test_repr(self):
        """Test the __repr__ method for correct string representation."""
        option = MCOption(1, "Is this a test?")
        option_repr = repr(option)
        expected_repr = "MCOption(idx=1, prompt={'en': 'Is this a test?'}, answer=None)"
        self.assertEqual(option_repr, expected_repr)
    
    def test_set_answer(self):
        """Test that the set_answer method works correctly."""
        option = MCOption(1, "Is this a test?")
        option.set_answer(True)
        self.assertTrue(option.answer)
        option.set_answer(False)
        self.assertFalse(option.answer)
    
    def test_set_answer_invalid(self):
        """Test that the set_answer method raises an error with invalid inputs."""
        option = MCOption(1, "Is this a test?")
        with self.assertRaises(ValueError):
            option.set_answer("Invalid")
    
    def test_set_prompt(self):
        """Test that the set_prompt method works correctly for different languages."""
        option = MCOption(1, "Is this a test?")
        option.set_prompt("Är detta ett test?", "sv")
        self.assertEqual(option.prompt.get("sv"), "Är detta ett test?")
        self.assertEqual(option.prompt.get("en"), "Is this a test?")
    
    def test_set_prompt_invalid_language(self):
        """Test that the set_prompt method raises an error for unsupported languages."""
        option = MCOption(1, "Is this a test?")
        with self.assertRaises(ValueError):
            option.set_prompt("C'est un test?", "fr")

if __name__ == "__main__":
    unittest.main()

