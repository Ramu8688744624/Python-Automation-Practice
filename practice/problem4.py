import csv

try:
    f=open("D:/Python for Automation/practice/family.csv")
    data=csv.reader(f)
    validrows=0
    invalidrows=0
    
    for row in data:
        try:
            name,age,sal=row
            sal=int(sal)
            age=int(age)
            validrows=validrows+1
        except(TypeError,ValueError):
            print("Skipping Bad Rows: ",row)
            invalidrows=invalidrows+1
    print("Valid Rows: ",validrows)
    print("Invalid Rows: ",invalidrows)
except FileNotFoundError:
    print("File Not Found")
            