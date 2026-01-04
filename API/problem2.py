import requests
import mysql.connector
url = "https://jsonplaceholder.typicode.com/users"
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="automation_db"
        )
    cursor=conn.cursor()
    print("Database Connected Successfully")
    
    response=requests.get(url)
    print("Status Code: ",response.status_code)
    data = response.json()
    
    for user in data:
        try:
            id = user["id"]
            name = user["name"]
            email = user["email"]
            city = user["address"]["city"]
            
            query="insert into api_users(id,name,email,city) values(%s,%s,%s,%s)"
            cursor.execute(query,(id,name,email,city))
        except mysql.connector.IntegrityError:
            print("SKipping Duplicate Records: ",id)
    conn.commit()
except Exception as e:
    print("Error: ",e)
    if 'conn' in locals():
        conn.rollback()
finally:
    if 'conn' in locals():
        conn.close()
    if 'cursor' in locals():
        cursor.close()
    
    