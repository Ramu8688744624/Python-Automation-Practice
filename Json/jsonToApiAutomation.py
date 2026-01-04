import json
import requests

try:
    with open("D:/Python for Automation/Json/family.json","r") as f:
        data=json.load(f)
    
    # API endpoint
    url = "https://httpbin.org/post"
    
    response=requests.post(url,json=data)
    
    print("Status: ",response.status_code)
    print("Response JSON:")
    print(response.json())
except FileNotFoundError:
    print("File Not Found Error")