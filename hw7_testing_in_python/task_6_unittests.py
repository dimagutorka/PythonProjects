import unittest
from unittest.mock import patch
import requests


class TestStringMethods(unittest.TestCase):

	@staticmethod
	def check_balance():
		"""
		Makes a GET request to fetch balance information and returns the response in JSON format.
		"""
		r = requests.get('https://httpbin.org/get')
		return r.json()

	def test_get_user_data(self):
		"""
		Tests the check_balance method to ensure it retrieves the correct data.
		"""
		with patch('requests.get') as mocked_get:
			# Mock the .json() method's return value
			mocked_get.return_value.json.return_value = {'balance': 999}

			# Call the method
			data = self.check_balance()

			# Assert that requests.get was called with the correct URL
			mocked_get.assert_called_with('https://httpbin.org/get')

			# Assert the data matches the expected mocked data
			self.assertEqual(data, {'balance': 999})


if __name__ == '__main__':
	unittest.main()
