import requests
url="https://jsonplaceholder.typicode.com/posts"
 
response=requests.get(url)
print(response.status_code)
 
if response.status_code == 200:
    data = response.json()
    print(len(data))
    for user in data[:3]:
        print(user['title'])
         