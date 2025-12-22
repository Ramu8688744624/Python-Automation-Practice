"""
📌 Requirement

Write a program that:

Opens a file named "data.txt"

Reads all content

Prints number of characters in the file

Rules:

Use with open()

If file not found → show a friendly message

Do not use exception chaining

📌 Concepts tested: open, read, FileNotFoundError
"""

try:
    f1=open("data.txt","r")
except FileNotFoundError as e:
    print("File Not Found")
else:
    content=f1.read()
    print(content)
    print(len(content))
    f1.close()

