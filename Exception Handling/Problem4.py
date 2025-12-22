"""
📌 Problem

Create a function withdraw(balance, amount).

Rules:

If amount <= 0 → raise InvalidAmountException

If amount > balance → raise InsufficientBalanceException

If valid → print remaining balance

🎯 Concepts Tested

Multiple custom exceptions

Multiple raise

Multiple except

❗ Rules

Each exception must have a meaningful message

Handle each exception separately
"""

class InvalidAmountException(Exception):
    pass
class InsufficientBalanceException(Exception):
    pass
def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountException('Please Enter Valid Amount')
    elif amount > balance:
        raise InsufficientBalanceException('Insufficient Funds')
    else:
        print(f"Remaining balance: {balance-amount}")
balance=int(input('Enter Total Balance: '))
amount=int(input('Enter Amount to be Withdrawn: '))
try:
    withdraw(balance,amount)
except InvalidAmountException as e:
    print(e)
except InsufficientBalanceException as e:
    print(e)