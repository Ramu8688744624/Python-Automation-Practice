import csv
try:
	f1=open("D:\Python for Automation\CSV\input.csv","r")
except FileNotFoundError as e:
	print(e)
else:
	dt_r=csv.reader(f1)

try:
	f2=open("D:\Python for Automation\CSV\output.csv","w",newline="")
except FileNotFoundError as e:
	print(e)
else:
	dt_w=csv.writer(f2)

next(dt_r)
dt_w.writerow(["Name","Age","Salary"])
for row in dt_r:
	try:
		sal=int(row[2])
		if sal>30000:
			dt_w.writerow(row)
	except (ValueError, IndexError):
		print("Skipping bad row:", row)