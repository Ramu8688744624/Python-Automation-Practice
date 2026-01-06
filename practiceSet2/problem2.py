import requests
url="https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for user in data:
        if user['email'] is not None or user['email'] != '':
            print(user['id'])
            print(user['email'])
            print('----------------')
        else:
            print('Email is Missing')