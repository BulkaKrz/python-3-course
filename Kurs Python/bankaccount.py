
class Result:
    def __init__(self, message, value=None):
        self.isSuccess = None
        self.message = message
        self.value = value
    def is_ok(self):
        return self.isSuccess

class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = False


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """tu sprawdzqamy czy pieniądze są prawdziwe"""
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return Ok("wypłacono kasę", amount)

        return Error("nie wypłacono kasy", amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Error("Nie udało się, próba przekroczenia progu", amount)
