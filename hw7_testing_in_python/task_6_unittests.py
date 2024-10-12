import unittest
from unittest.mock import patch
import requests


class TestStringMethods(unittest.TestCase):

	@staticmethod
	def check_balance():
		r = requests.get('https://httpbin.org/get')
		return r.json

	def test_get_user_data(self):
		with patch('requests.get') as mocked_get:
			mocked_get.return_value.json = {'balance': 999}
			data = self.check_balance()
			mocked_get.assert_called_with('https://httpbin.org/get')
			self.assertEqual(data, {'balance': 999})


if __name__ == 'main.py':
	unittest.main()
