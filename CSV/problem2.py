import csv
f1=open("C:\\Users\\ramua\\Downloads\\Family.csv","r")
data=csv.reader(f1)
next(data)
for row in data:
	sal=int(row[2])
	print(sal,type(sal))