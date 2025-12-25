"""
🌟 LESSON 6 — Salary Calculations (Child Level)

Now we will calculate:

1️⃣ Total salary
2️⃣ Highest salary
3️⃣ Lowest salary
4️⃣ Average salary
"""
import csv
f1=open("C:\\Users\\ramua\\Downloads\\Family.csv","r")
data=csv.reader(f1)
total=0
count=0
max=0
min=99999

next(data)

for row in data:
    sal = int(row[2])

    total = total + sal
    count = count + 1

    if sal > max:
        max = sal

    if sal < min:
        min = sal

	
		
    

print("Total=",total)
print("Count=",count)
print("maximum Salary=",max)
print("Minimum Salary=",min)