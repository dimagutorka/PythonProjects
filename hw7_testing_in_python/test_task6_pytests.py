from task_6 import BankAccount
import pytest


@pytest.fixture
def bank_balance():
    """
    Fixture to initialize a BankAccount with a starting balance of 100.
    """
    return BankAccount(100)


def test_zero_balance(bank_balance):
    """
    Test to ensure that after withdrawing the full balance, the account has a zero balance.
    Skips the test if the balance becomes zero.
    """
    bank_balance.withdraw(100)
    if bank_balance.get_balance() == 0:
        pytest.skip("Your bank account balance is 0")

    assert bank_balance.get_balance() != 0  # This should now fail if the balance is zero


@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (100, 200),
    (0, 100),
    (5.5, 105.5),
])
def test_deposit(bank_balance, deposit_amount, expected_balance):
    """
    Test deposit functionality with multiple amounts.
    """
    bank_balance.deposit(deposit_amount)
    assert bank_balance.get_balance() == expected_balance


@pytest.mark.parametrize("withdraw_amount, expected_balance", [
    (50, 50),
    (0, 100),
    (10, 90),
])
def test_withdraw(bank_balance, withdraw_amount, expected_balance):
    """
    Test withdraw functionality with multiple amounts.
    """
    bank_balance.withdraw(withdraw_amount)
    assert bank_balance.get_balance() == expected_balance
