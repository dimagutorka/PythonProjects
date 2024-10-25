import pytest


class UserManager:
    """
    A simple class to manage users, allowing adding, removing, and retrieving users.
    """

    list_with_users = []

    def add_user(self, first_name: str, last_name: str) -> None:
        """
        Adds a new user with the given first and last name to the user list.

        Args:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
        """
        new_user = f'{first_name} {last_name}'
        UserManager.list_with_users.append(new_user)

    def remove_user(self, user: str) -> None:
        """
        Removes a user from the user list.

        Args:
            user (str): The full name of the user to remove.
        """
        UserManager.list_with_users.remove(user)

    def get_all_users(self) -> None:
        """
        Prints the list of all users.
        """
        print(UserManager.list_with_users)


@pytest.fixture
def user_manager():
    """
    Fixture to provide a UserManager instance and ensure `list_with_users` is cleared after each test.
    """
    mr_manager = UserManager()
    yield mr_manager
    # Clear list_with_users after each test to ensure isolation
    UserManager.list_with_users.clear()


@pytest.fixture
def user_creation(user_manager):
    """
    Fixture to add a set of users to the UserManager instance.
    """
    user_manager.add_user('Anton', 'Antonov')
    user_manager.add_user('Ivan', 'Ivanov')
    user_manager.add_user('Anton', 'Antonov')
    user_manager.add_user('Ivan', 'Ivanov')
    yield  # Allow tests to run with these users pre-added


def test_add_user(user_creation):
    """
    Test that four users are added correctly.
    """
    assert len(UserManager.list_with_users) == 4


def test_remove_user(user_creation, user_manager):
    """
    Test removing a user from the list of users.
    """
    user_manager.remove_user('Ivan Ivanov')
    assert len(UserManager.list_with_users) == 3


def test_numbers_of_users(user_creation):
    """
    Test that skips if the number of users is 3 or more, otherwise checks exact count.
    """
    if len(UserManager.list_with_users) >= 3:
        pytest.skip('Not implemented yet')

    assert len(UserManager.list_with_users) == 3
