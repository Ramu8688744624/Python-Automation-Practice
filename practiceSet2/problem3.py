import requests
import csv
url="https://jsonplaceholder.typicode.com/posts"
try:
    with open('posts.csv','w') as f:
        data = csv.writer(f)
        data.writerow(["id","title","userId"])
        response = requests.get(url)
        if response.status_code == 200:
            total_posts = response.json()
            for post in total_posts:
                data.writerow([post['id'],post['title'],post['userId']])
        else:
            print('api failed please find status code: ',response.status_code)
except FileNotFoundError:
    print("File Not Found")
    