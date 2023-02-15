import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 77, "name": "Josiah", "views": 100000},
        {"likes": 100000, "name": "How to make REST API", "views": 800000},
        {"likes": 30, "name": "Tim does a back flip", "views": 20000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())
