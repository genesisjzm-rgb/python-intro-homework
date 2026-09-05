import requests

url = "https://api.agify.io/?name=michael"
response = requests.get(url)

print("Status code:", response.status_code)
# Output: Status code: 200

data = response.json()
print(data)

