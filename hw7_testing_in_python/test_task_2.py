import requests
import unittest
from unittest.mock import patch


def get_data():
    """
    Makes a GET request to a specific URL and returns the status code if successful,
    or the response text if there was an error.
    """
    r = requests.get('https://httpbin.org/get')
    if r.ok:
        return r.status_code
    else:
        return r.text


class TestUserData(unittest.TestCase):

    def test_get_user_data(self):
        """
        Tests the get_data function by mocking the requests. get method.
        """
        with patch('requests.get') as mocked_get:
            # Case 1: Successful request with status code 200
            mocked_get.return_value.ok = True
            mocked_get.return_value.status_code = 200
            data = get_data()
            mocked_get.assert_called_with('https://httpbin.org/get')
            self.assertEqual(data, 200)

            # Case 2: Successful request with status code 404
            mocked_get.return_value.ok = True
            mocked_get.return_value.status_code = 404
            data = get_data()
            mocked_get.assert_called_with('https://httpbin.org/get')
            self.assertEqual(data, 404)

            # Case 3: Unsuccessful request with response text
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Error: Not Found"
            data = get_data()
            mocked_get.assert_called_with('https://httpbin.org/get')
            self.assertEqual(data, "Error: Not Found")


if __name__ == '__main__':
    unittest.main()
