import requests

user_id=5
url=f"https://jsonplaceholder.typicode.com/users/{user_id}"

response=requests.get(url)

if response.status_code == 200:
    data =response.json()
    print(data['name'])
    print(data['email'])
else:
    print('status code Error: ',response.status_code)
    