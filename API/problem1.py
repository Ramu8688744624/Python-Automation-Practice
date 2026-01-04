import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response=requests.get(url)
    print("Status Code: ",response.status_code)
    # print("Response: ")
    #print(response.json())
    
    data = response.json()
    total=0
    for user in data:
        print("Name: ",user["name"])
        print("Email: ",user["email"])
        print("City: ",user["address"]["city"])
        print("------------------------")
        total=total+1
    print("Total Records: ",total)
    
    
except Exception as e:
    print("Error Raise: ",e)