import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="automation_db"
        )
        
    cursor=conn.cursor()
        
    print("Database Connected")
        
    query="""
    update employee_data set salary = salary + (salary*0.10)
    where salary > 30000
    """
    cursor.execute(query)
    conn.commit()
    
    print("Salary Updated Successfully")
    print("Affected Rows: ",cursor.rowcount)
except Exception as e:
    print("Error:",e)
    conn.rollback()
finally:
    conn.close()
    cursor.close()