import csv
try:
    f1= open("D:/Python for Automation/practice/problem1.csv")
    fb=csv.reader(f1)
    for row in fb:
        try:
            sal=int(row[2])
            print("Name:",row[0])
            print("salary:",row[2])
        
        except(ValueError,TypeError):
            print("Invalid Salary",row[2])
        
    

except FileNotFoundError:
    print("File Not Found")
