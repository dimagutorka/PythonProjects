from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token
from drf_app.models import Book


class TestSetUp(APITestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = User.objects.create_user(username='dima_testcases1',
		                                    email='dimatestcases@1gmail.com',
		                                    password='91589185185Fs')
		cls.token, _ = Token.objects.get_or_create(user=cls.user)

		cls.data_book_for_db = {"title": "TEST Book",
		                        "author": "TEST Author",
		                        "genre": "TEST genre",
		                        "publication_year": 2000,
		                        "user_id": cls.user.id}

		cls.book = Book.objects.create(**cls.data_book_for_db)
		cls.book_list_url = reverse('book-list')
		cls.book_detail_url = f"/books/{cls.book.id}/"

	def setUp(self):
		self.book_data = {"title": "TEST Book",
		                 "author": "TEST Author",
		                 "genre": "TEST genre",
		                 "publication_year": 2000,
		                 "user": self.user.id}

		self.book_data_put =  {"title": "NEW Book",
		                 "author": "NEW Author",
		                 "genre": "NEW genre",
		                 "publication_year": 1000,
		                 "user": self.user.id}

		# self.client.force_authenticate(user=self.user)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
		return super().setUp()

	def tearDown(self):
		return super().tearDown()


class TestBookPositiveCases(TestSetUp):

	def test_create_book(self):
		response = self.client.post(self.book_list_url, self.book_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_retrieve_book(self):
		response = self.client.get(self.book_detail_url)
		self.book_data['id'] = response.data['id']  # add a field from response to compare two dicts
		self.book_data['created_at'] = response.data['created_at']  # add a field from response to compare two dicts

		self.assertEqual(response.data, self.book_data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_book(self):
		response = self.client.put(self.book_detail_url, self.book_data_put, format='json')
		self.book_data_put['id'] = response.data['id']  # add a field from response to compare two dicts
		self.book_data_put['created_at'] = response.data['created_at']  # add a field from response to compare two dicts

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, self.book_data_put)

	def test_book_by_filter_contain(self):
		response = self.client.get(self.book_detail_url, {'title__icontains': "TEST"})
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_book_without_perms(self):
		response = self.client.delete(self.book_detail_url)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_delete_book_with_perms(self):
		self.superuser = User.objects.create_superuser(
			username="admin",
			password="adminpassword"
		)

		self.client.force_authenticate(user=self.superuser)
		response = self.client.delete(self.book_detail_url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestAuth(APITestCase):

	def test_no_token(self):
		response = self.client.get(reverse('book-list'))
		self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

	def test_invalid_token(self):
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'Invalid Token')
		response = self.client.get(reverse('book-list'))
		self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)