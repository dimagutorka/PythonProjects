class BankAccount:
    """
    A simple BankAccount class for managing balance operations such as deposit, withdrawal,
    and balance inquiry. Supports addition and subtraction of balances between accounts.
    """

    def __init__(self, balance: float = 0.0) -> None:
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            balance (float): The initial balance. Defaults to 0.0.
        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposits an amount to the bank account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws an amount from the bank account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If amount is negative or if withdrawal exceeds the current balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance.

        Returns:
            float: The current balance.
        """
        return self.balance

    def __add__(self, other: "BankAccount") -> "BankAccount":
        """
        Allows adding the balances of two BankAccount objects.

        Args:
            other (BankAccount): Another BankAccount instance.

        Returns:
            BankAccount: A new BankAccount instance with the combined balance.
        """
        if not isinstance(other, BankAccount):
            return NotImplemented
        return BankAccount(self.balance + other.balance)

    def __sub__(self, other: "BankAccount") -> "BankAccount":
        """
        Allows subtracting the balance of another BankAccount from this one.

        Args:
            other (BankAccount): Another BankAccount instance.

        Returns:
            BankAccount: A new BankAccount instance with the resulting balance.

        Raises:
            ValueError: If the resulting balance would be negative.
        """
        if not isinstance(other, BankAccount):
            return NotImplemented
        if self.balance < other.balance:
            raise ValueError("Resulting balance cannot be negative.")
        return BankAccount(self.balance - other.balance)
