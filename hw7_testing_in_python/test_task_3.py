import pytest


class UserManager:

	list_with_users = []

	def add_user(self, first_name, last_name):
		new_user = f'{first_name} {last_name}'
		UserManager.list_with_users.append(new_user)

	def remove_user(self, user):
		UserManager.list_with_users.remove(user)

	def get_all_users(self):
		print(UserManager.list_with_users)


@pytest.fixture
def user_manager():
	mr_manager = UserManager()
	return mr_manager


@pytest.fixture
def user_creation(user_manager):
	user_manager.add_user('Anton', 'Antonov')
	user_manager.add_user('Ivan', 'Ivanov')
	user_manager.add_user('Anton', 'Antonov')
	user_manager.add_user('Ivan', 'Ivanov')


def test_add_user(user_creation, user_manager):
	assert len(UserManager.list_with_users) == 4


def test_remove_user(user_manager):
	user_manager.remove_user('Ivan Ivanov')
	assert len(UserManager.list_with_users) == 3


def test_numbers_of_users(user_manager):
	if len(UserManager.list_with_users) >= 3:
		pytest.skip('Not implemented yet')

	assert len(UserManager.list_with_users) == 3
