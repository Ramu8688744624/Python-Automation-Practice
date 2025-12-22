import csv
f1=open("D:\Downloads\Crime_Data_from_2020_to_Present.csv",'r')
data=csv.reader(f1)
#used to print the starting lines of the csv file
print(next(data))  # To skip the header row
#used to print all the lines of the csv file
for line  in data:
    print(line)