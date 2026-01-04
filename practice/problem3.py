import json

data = [
  {"name": "A", "salary": 30000},
  {"name": "B", "salary": 45000}
]
try:
    with open("D:/Python for Automation/practice/demo.json","w") as f:
        json.dump(data,f,indent=4)
except FileNotFoundError:
    print("File Not Found Error")
