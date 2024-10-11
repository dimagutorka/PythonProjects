import requests
import unittest
from unittest.mock import patch


def get_data():
	r = requests.get('https://httpbin.org/get')
	if r.ok:
		return r.status_code
	else:
		return r.text


class TestUserData(unittest.TestCase):

	def test_get_user_data(self):
		with patch('requests.get') as mocked_get:

			mocked_get.return_value.ok = True
			mocked_get.return_value.status_code = '200'
			data = get_data()
			mocked_get.assert_called_with('https://httpbin.org/get')
			self.assertEqual(data, '200')

			mocked_get.return_value.ok = True
			mocked_get.return_value.status_code = '404'
			data = get_data()
			mocked_get.assert_called_with('https://httpbin.org/get')
			self.assertEqual(data, '404')

			mocked_get.return_value.ok = False
			mocked_get.return_value.text = {"data": "test"}
			data = get_data()
			mocked_get.assert_called_with('https://httpbin.org/get')
			self.assertEqual(data, {"data": "test"})


if __name__ == 'main.py':
	unittest.main()

