
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def new_user_factory(db):
	def create_app_user(
			username,
			password=None,
			email='test@gmai.com',
			first_name='test',
			last_name='test',
			is_active=True,
			is_staff=True,
			is_superuser=True
	):

		user = User.objects.create_user(
			username=username,
			password=password,
			email=email,
			first_name=first_name,
			last_name=last_name,
			is_active=is_active,
			is_staff=is_staff,
			is_superuser=is_superuser
		)

		return user
	return create_app_user


@pytest.fixture
def new_user(db, new_user_factory):
	return new_user_factory(username='dima')


@pytest.fixture
def new_user1(db, new_user_factory):
	return new_user_factory(is_staff=True)