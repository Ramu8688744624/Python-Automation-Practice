"""📌 Problem

Write a program that:

Takes two integers from user

Divides the first number by the second

Handles division by zero gracefully"""

n1=int(input("Enter First Number: "))
n2=int(input('Enter Second Number: '))
try:
    result=(n1/n2)
except ZeroDivisionError as e:
    print("Second Number should not be equal to zero")
else:
    print("Result is:", result)
finally:
    print("Execution finished")