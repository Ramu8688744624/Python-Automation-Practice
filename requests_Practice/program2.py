import requests

url="https://jsonplaceholder.typicode.com/posts"

data={
    "title": "Automation Engineer",
  "body": "Learning API automation",
  "userId": 1
}

response=requests.post(url,json=data)

if response.status_code==201:
    print(response.json())
else:
    print("Failed to create a post. Status code:", response.status_code)