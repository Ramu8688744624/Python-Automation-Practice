import requests

resposnse=requests.get("https://jsonplaceholder.typicode.com/posts")

data=resposnse.json()
total=0

for row in data:
    print(row["id"])
    print(row["userId"])
    print(row["title"])
    print("-------------------")
    total+=1
print("Total posts:",total)