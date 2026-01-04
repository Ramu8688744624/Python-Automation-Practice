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
    
    f1=open("D:/Python for Automation/CSV/input.csv")
    data=csv.reader(f1)
    next(data)
    success=0
    failed=0
    
    for row in data:
        try:
            name,age,salary = row
            salary=int(salary)
            age=int(age)
            query="""
            insert into employee_data(name,age,salary)
            values(%s,%s,%s)
            """
            cursor.execute(query,(name,age,salary))
            success=success+1
        except(TypeError,ValueError):
            print("Skipped Bad Row: ",row)
            failed=failed+1
    conn.commit()
    print("Data Inserted Successfully")
    print("Valid Rows: ",success)
    print("Invalid Rows: ",failed)
except Exception as e:
    print("Exception Raised: ",e)
    conn.rollback()

finally:
    f1.close()
    cursor.close()
    conn.close()
    

    