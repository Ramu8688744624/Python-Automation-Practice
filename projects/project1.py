import csv
try:
    f1=open("D:\Python for Automation\projects\Family.csv","r")
except FileNotFoundError:
    print("Main File is Not Found")
else:
    reader=csv.reader(f1)

try:
    f2=open("D:\Python for Automation\projects\clean_data.csv","w",newline="")
except FileNotFoundError:
    print("Clean File is Not Found")
else:
    writer_clean=csv.writer(f2)



try:
    f3=open("D:\Python for Automation\projects\high_salary.csv","w",newline="")
except FileNotFoundError:
    print("High Salary File is Not Found")
else:
    writer_high=csv.writer(f3)

next(reader)
totalsalary=0
maxsalary=0
minsalary=10**9
count=0

writer_clean.writerow(["Name","Age","Salary"])
writer_high.writerow(["Name","Age","Salary"])
for row in reader:
    try:
        sal=int(row[2])
        totalsalary=totalsalary+sal
        count=count+1
        if sal>maxsalary:
            maxsalary=sal
        if sal<minsalary:
            minsalary=sal
        writer_clean.writerow(row)
        if sal>30000:
            writer_high.writerow(row)
    except(ValueError,IndexError):
         print("Skipping bad row:", row)

print("Total Salary:", totalsalary)
print("Maximum Salary:", maxsalary)
print("Minimum Salary:", minsalary)
print("count of valid rows:", count)
print("Data Cleaning Completed")
f1.close()
f2.close()
f3.close()
    
    