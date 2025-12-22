import csv
f1=open("C:\\Users\\ramua\\Downloads\\Family.csv","r")
data=csv.reader(f1)
# this below is to print all the csv file data
for row in data:
    print(row)

#after running above loop cursor control reaches to the end of the file that's why we are writing below two startements to bring again cursor control to the starting.
f1.seek(0)
data=csv.reader(f1)
# below code is to print only starting column of the csv file
for row in data:
	print(row[0])
      

"""
If you want only names (without header), output should be:
Ramu
Shyamu
Kamal
Venugopal

METHOD 1 → Use next()

import csv

f = open("Family.csv", "r")
data = csv.reader(f)

next(data)   # skips first row

for row in data:
    print(row[0])

f.close()


METHOD 2 → Skip using index

"""
f1.close()