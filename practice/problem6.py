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
    
    emp_id=int(input('Enter Employee ID you want to add Increment: '))
    increment=int(input('Enter Increment Amount: '))
    
    query="""
    update employee_data set salary = salary + %s where
    id = %s """
    
    cursor.execute(query,(increment,emp_id))
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        conn.commit()
    else:
        conn.rollback()

except Exception as e:
    if 'conn' in locals():
        print("Error:",e)
        conn.rollback()
finally:
    if 'conn' in locals():
        conn.close()
    if 'cursor' in locals():
        cursor.close()