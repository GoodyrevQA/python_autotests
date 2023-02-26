import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 333,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Sharik",
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
})
# print(response.text)

url_hh = "https://api.hh.ru/suggests/skill_set"
skill = "Экстремальное программирование"
response2 = requests.get(url_hh, headers={"HH-User-Agent":"PostmanRunTime/7.29.2"},
    params={"text":skill})
# print(response2.text)

