import requests
url="https://jsonplaceholder.typicode.com/comments"
params={
    'postId':"1"
}
response = requests.get(url,params=params)
data=response.json()
total=0
if response.status_code == 200:
    print(response.json())
    for user in data:
        total=total+1

print('Status Code:',response.status_code)
print("Total Records: ",total)