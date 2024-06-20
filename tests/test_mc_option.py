import unittest
from question.mc_option import MCOption

class TestMCOption(unittest.TestCase):

    def setUp(self):
        self.option = MCOption(idx=1, prompt="Option 1", answer=True, lang='en')

    def test_mc_option_init(self):
        self.assertEqual(self.option.idx, 1)
        self.assertEqual(self.option.prompt, {'en': "Option 1"})
        self.assertTrue(self.option.answer)
        self.assertEqual(self.option._answer, True)

    def test_mc_option_repr(self):
        expected_repr = "MCOption(idx=1, prompt={'en': 'Option 1'}, answer=True)"
        self.assertEqual(repr(self.option), expected_repr)

    def test_mc_option_set_answer(self):
        self.option.set_answer(False)
        self.assertFalse(self.option.answer)
        self.assertEqual(self.option._answer, False)

    def test_mc_option_answer_property(self):
        self.assertEqual(self.option.answer, True)
        self.option.set_answer(False)
        self.assertEqual(self.option.answer, False)

if __name__ == '__main__':
    unittest.main()
