import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="automation_db"
        )
        
    cursor=conn.cursor()
    print("Database connected successfully")
    
    query1="""
    update employee_data set salary = salary + 1000
    where salary<30000
    """
    
    cursor.execute(query1)
    print("Affected Rows:",cursor.rowcount)
    query2="""
    update employee_data set sal=sal+1000
    where id=1"""
    
    cursor.execute(query2)
    conn.commit()
    
    print("Data Updated Successfully")
    
except Exception as e:
    print("Error:",e)
    conn.rollback()
finally:
    conn.close()
    cursor.close()
    