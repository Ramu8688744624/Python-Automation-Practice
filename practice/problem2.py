import csv
try:
    f1=open("D:/Python for Automation/CSV/input.csv")
    data=csv.reader(f1)
    
    totalsal=0
    count=0
    next(data)  # Skip header row
    for row in data:
        try:
             name,age,salary = row
             sal=int(salary)
             totalsal=sal+totalsal
             count=count+1
             
        except(TypeError,ValueError):
            print("Skipping Bad Row: ", row )
except FileNotFoundError:
    print("File Not Found")
    
             
        