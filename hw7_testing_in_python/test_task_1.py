import unittest
from task_1_functions import StringProcessor


class TestString(unittest.TestCase):

    def setUp(self) -> None:
        """
        Set up the test fixture for each test.
        Initializes the StringProcessor with 'qqqq' and precomputes
        reversed, capitalized, and original strings for testing.
        """
        self.class_object = StringProcessor('qqqq')
        self.reversed_string = self.class_object.reverse_string()
        self.capitalized_string = self.class_object.capitalize_string()
        self.original_string = self.class_object.string

    @unittest.skip('Not finished yet')
    def test_reversed_str_not_empty(self):
        """
        Test that the reversed string is not empty.
        """
        self.assertNotEqual(self.reversed_string, '')

    def test_reversed_str_single_case(self):
        """
        Test that the reversed string is entirely in one case (all uppercase or all lowercase).
        """
        single_case = self.reversed_string.islower() or self.reversed_string.isupper()
        self.assertTrue(single_case, 'The reversed string should be entirely in one case.')

    def test_reversed_no_symbols_or_digits(self):
        """
        Test that the reversed string does not contain any symbols or digits.
        """
        contains_invalid_chars = not self.reversed_string.isalpha()
        self.assertFalse(contains_invalid_chars, 'The reversed string should not contain symbols or digits.')

    def test_capitalized_str_not_empty(self):
        """
        Test that the capitalized string is not empty.
        """
        self.assertNotEqual(self.capitalized_string, '')

    def test_capitalized_str_single_case(self):
        """
        Test that the capitalized string has only the first letter capitalized.
        """
        single_case = self.capitalized_string.islower() or self.capitalized_string.isupper()
        self.assertFalse(single_case, 'The capitalized string should not be in one register (it should be title case).')

    def test_capitalized_no_symbols_or_digits(self):
        """
        Test that the capitalized string does not contain symbols or digits.
        """
        contains_invalid_chars = not self.capitalized_string.isalpha()
        self.assertFalse(contains_invalid_chars, 'The capitalized string should not contain symbols or digits.')

    def test_original_str_not_empty(self):
        """
        Test that the original string is not empty.
        """
        self.assertNotEqual(self.original_string, '')

    def test_original_str_single_case(self):
        """
        Test that the original string is entirely in one case (either all lowercase or all uppercase).
        """
        single_case = self.original_string.islower() or self.original_string.isupper()
        self.assertTrue(single_case, 'The original string should be entirely in one case.')

    def test_original_no_symbols_or_digits(self):
        """
        Test that the original string does not contain symbols or digits.
        """
        contains_invalid_chars = not self.original_string.isalpha()
        self.assertFalse(contains_invalid_chars, 'The original string should not contain symbols or digits.')


if __name__ == '__main__':
    unittest.main()
