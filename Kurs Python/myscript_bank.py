"""konto bankowe"""
#from bankaccount import BankAccount

from bankaccount import MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)


result = accountMin.try_withdraw(300)




if (result.is_ok()):
    print(result.message)


"""

konto = BankAccount(1000)

konto.deposit(500)

amountToWithdraw = 300

isSuccess, mesage, value = konto.try_withdraw(amountToWithdraw)

print(isSuccess)
print(mess)



if konto.try_withdraw(7000):
    print("tak wypłacono kasę")
    print("aktualny stan konta wynosi",konto)
else:
    print("za mało na koncie")
    """
