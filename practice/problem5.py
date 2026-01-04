import csv
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="automation_db"
        )
    cursor=conn.cursor()
    print("Database Connected Successfully")
    
    f=open("D:/Python for Automation/practice/family.csv")
    data=csv.reader(f)
    inserted=0
    skippedRows=0
    next(data)  # Skip header row if present
    for row in data:
        try:
            name,age,sal=row
            sal=int(sal)
            age=int(age)
            query="""
            insert into employee_data(name,age,salary)
            values(%s,%s,%s)"""
            cursor.execute(query,(name,age,sal))
            inserted=inserted+1
        except Exception as e:
            skippedRows=skippedRows+1
            print("Error:",e)
    conn.commit()
    print("Inserted Rows:",inserted)
    print("Skipped Rows:",skippedRows)  
except Exception as e:
    print("Exception Raised: ",e)
    conn.rollback()
finally:
    conn.close()
    f.close()
    
            
            