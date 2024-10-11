import unittest
from task_1_functions import *


class TestString(unittest.TestCase):

	def setUp(self) -> None:
		self.class_object = StringProcessor('qqqq')
		self.reversed_string = self.class_object.reverse_string()
		self.capitalized_string = self.class_object.capitalize_string()
		self.vowel_in_str = self.class_object.string

	@unittest.skip('Not finished yet')
	def test_reversed_str_empty(self):
		self.assertNotEqual(self.reversed_string, '')

	def test_reversed_str_one_register(self):
		only_one_register = True
		if not self.reversed_string.islower() and not self.reversed_string.isupper():
			only_one_register = False
		self.assertEqual(only_one_register, True, 'Your string should be in only one register')

	def test_reversed_no_symbl_digit(self):
		is_any_digit_ot_symbol = False
		if not self.reversed_string.isalnum() or self.reversed_string.isdigit():
			is_any_digit_ot_symbol = True
		self.assertEqual(is_any_digit_ot_symbol, False, 'Your string cannot contain any digits or symbols')

	def test_capitalized_str_empty(self):
		self.assertNotEqual(self.capitalized_string, '')

	def test_capitalized_str_one_register(self):
		only_one_register = True

		if not self.capitalized_string.islower() and not self.capitalized_string.isupper():
			only_one_register = False
		self.assertNotEqual(only_one_register, True, 'Your string should be in only one register')

	def test_capitalized_no_symbl_digit(self):
		is_any_digit_ot_symbol = False
		if not self.capitalized_string.isalnum() or self.capitalized_string.isdigit():
			is_any_digit_ot_symbol = True
		self.assertEqual(is_any_digit_ot_symbol, False, 'Your string cannot contain any digits or symbols')

	def test_count_vowel_str_empty(self):
		self.assertNotEqual(self.vowel_in_str, '')

	def test_count_vowel_one_register(self):
		only_one_register = True
		if not self.vowel_in_str.islower() and not self.vowel_in_str.isupper():
			only_one_register = False
		self.assertEqual(only_one_register, True, 'Your string should be in only one register')

	def test_count_vowel_symbl_digit(self):
		is_any_digit_ot_symbol = False
		if not self.vowel_in_str.isalpha() and self.vowel_in_str.isdigit():
			is_any_digit_ot_symbol = True
		self.assertEqual(is_any_digit_ot_symbol, False, 'Your string cannot contain any digits or symbols')


if __name__ == '__main__':
	unittest.main()

