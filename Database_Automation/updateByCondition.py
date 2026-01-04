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
    emp_id=int(input("for which user you want to update please enter id:"))
    sal=int(input("How much salary you want to update? please enter updated amount: "))
    query="""
    update employee_data set salary=salary+%s
    where id=%s
    """
    
    cursor.execute(query,(sal,emp_id))
    confirm=input("Are you sure want to update?uf yes please enter Yes else NO")
    if confirm.lower() == "yes":
        conn.commit()
        print("Data Updated Successfully, Affected rows:",cursor.rowcount)
    else:
        conn.rollback()
        print("Update Cancelled by User")
except Exception as e:
    print("Error:",e)
    conn.rollback()
finally:
    conn.close()
    cursor.close()
    