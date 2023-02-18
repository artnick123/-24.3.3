import requests
print('--- GET ---')
status='available'

res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())


print('--- POST ---')
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post( f"https://petstore.swagger.io/v2/pet", headers = {'accept': 'application/json'},data=data)
print(res.status_code)
print(res.text)
print(res.json())


print('--- DELETE ---')
petId = 1
res = requests.delete( f"https://petstore.swagger.io/v2/pet/{petId}")
print(res.status_code)
print(res.text)
print(res.json())

print('--- PUT ---')
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put( f"https://petstore.swagger.io/v2/pet", headers = {'accept': 'application/json'},data=data)
print(res.status_code)
print(res.text)
print(res.json())