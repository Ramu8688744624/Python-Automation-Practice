"""
📌 Problem

Simulate user registration with exception handling.

Input:
Understanding:

Username (string)

Password (string)

Age (integer)

Rules:

Username must not be empty → InvalidUsernameException

Password length must be ≥ 8 → WeakPasswordException

Age must be ≥ 18 → InvalidAgeException

Any unexpected error must be handled generically

🎯 Concepts Tested

Multiple custom exceptions

Validation logic

Proper exception hierarchy

Generic fallback exception

❗ Rules

Create separate custom exception classes

Use try–except–else

Do not catch everything in one block

Print "Registration Successful" only if no exception occurs
"""


class InvalidUsernameException(Exception):
    pass
class WeakPasswordException(Exception):
    pass
class InvalidAgeException(Exception):
    pass
def userRegistration(Username,Password,Age):
    if Username is  None or Username == "":
        raise InvalidUsernameException("User Name should not be Empty")
    elif len(Password)<8:
        raise WeakPasswordException("Password Length Should be Minimum 8 Characters")
    elif Age < 18:
        raise InvalidAgeException("Age Should be Greater than or equal to 18")
name=input('Please Enter  Name: ')
passWord=input('Please Enter Password: ')
age=int(input('Please Enter Age: '))
try:
    userRegistration(name,passWord,age)
except InvalidUsernameException as e:
    print(e)
except WeakPasswordException as e:
    print(e)
except InvalidAgeException as e:
    print(e)
else:
    print("Registration Successful")