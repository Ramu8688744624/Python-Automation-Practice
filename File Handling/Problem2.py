"""
Write a Python function wordCount(filename) that:

Reads the file

Returns total number of words

Print:

Total words = X


Rules:

Words must be separated using whitespace

Use file exception handling

Do not use global variables

📌 Concepts tested: reading line-by-line, split(), return value
"""

def wordcount(dataFile):
    try:
        f=open(dataFile,'r')
    except FileNotFoundError as e:
        print("File Not Found")
    else:
        data=f.read()
        words=data.split()
        return len(words)
dFile="data.txt"
TotalWords=wordcount(dFile)
print("Total words =",TotalWords)