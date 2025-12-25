import csv
f=open("C:\\Users\\ramua\\Downloads\\output.csv","w",newline="")
dt=csv.writer(f)
dt.writerow(["Name","Age"])
dt.writerow(["Ramu","24"])
dt.writerow(["Shyamu","24"])
dt.writerow(["Venugopal","28"])