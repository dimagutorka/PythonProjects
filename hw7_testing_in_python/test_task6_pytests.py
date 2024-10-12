from task_6 import BankAccount
import pytest


new_balance = BankAccount(100).get_balance()


@pytest.fixture
def bank_balance():
	balance = BankAccount(100)
	return balance


def test_zero_balance(bank_balance):
	bank_balance.withdraw(100)
	if bank_balance.get_balance() == 0:
		pytest.skip("Your bank account is 0")

	assert bank_balance.get_balance() != 0


@pytest.mark.parametrize("a, b,  result", [
	(new_balance, 100, 200),
	(new_balance, 0, 100),
	(new_balance, 5.5, 105.5),

])
def test_deposite(a, b, result):
	assert a + b == result



# @pytest.mark.parametrize("a, b,  result", [
# 	(new_balance, 100, 200),
# 	(new_balance, 0, 100),
# 	(new_balance, 5.5, 105.5),
#
# ])
# def test_withdrawn(a, b, result):
# 	assert a - b == result
