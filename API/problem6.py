import requests
url= "https://jsonplaceholder.typicode.com/posts"
headers={
    "Authorization" : "Bearer dummy_token_123"
}

response = requests.get(url, headers=headers)
print(response.status_code)