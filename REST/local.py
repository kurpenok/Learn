import requests

result = requests.get("http://localhost:3000/api/courses/0")
print(result.json())

result = requests.post("http://localhost:3000/api/courses/3",
        {"name": "Kotlin", "videos": 5})
print(result.json())

result = requests.put("http://localhost:3000/api/courses/3",
        {"name": "Golang", "videos": 20})
print(result.json())

result = requests.delete("http://localhost:3000/api/courses/3")
print(result.json())

