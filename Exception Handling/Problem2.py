"""
📌 Problem

Take a number from user and:

Convert it to integer

Divide 100 by that number

Handle:

Invalid input (string, float, etc.)

Division by zero

🎯 Concepts Tested

Multiple except blocks

Built-in exceptions (ValueError, ZeroDivisionError)

❗ Rules

Use separate except blocks

No generic exception
"""


try:
    num=int(input('Enter Input: '))
    result=100/num
except ValueError as e:
    print("Cannot Convert String to Integer")
except ZeroDivisionError as e:
    print("Please Enter Number Which is not zero")
else:
    print("Result is:", result)
finally:
    print("Execution finished")
    