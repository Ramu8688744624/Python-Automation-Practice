"""📌 Problem

Create a custom exception InvalidMarksException.

Rules:

Marks must be between 0 and 100

If invalid, raise custom exception

If valid, print "Marks accepted"

🎯 Concepts Tested

Custom exception class

raise

Handling user-defined exception

❗ Rules

Do not use Exception directly

Use only your custom exception"""

class InvalidMarksException(Exception):
    pass
def checkMarks(marks):
    if marks<0 or marks>100:
        raise InvalidMarksException("Marks Should be between zero and Hundred!")
    else:
        print("Marks accepted")
marks=int(input('Enter your marks: '))
try:
    checkMarks(marks)
except InvalidMarksException as e:
    print(e)