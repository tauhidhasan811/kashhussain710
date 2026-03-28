import json

with open('data/mot_history.json', 'r') as f:
    data = json.load(f)

print(data['data'])
 
# import requests

# url = "https://kashhussain710-backend-nestjs.onrender.com/api/v1/check-car/free"

# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY5YmNkMGJhYWI3YzhjODljNmU1OGRjNSIsImVtYWlsIjoidXNlckBnbWFpbC5jb20iLCJyb2xlIjoidXNlciIsImlhdCI6MTc3NDY2OTEzOCwiZXhwIjoxNzc1MjczOTM4fQ.rXZiDwJPA0iUBtIjM1I_hVpjNRkmdlU0kG81jcSGP2s"
# }

# data = {
#     "registrationNumber": "AB12CDE"
# }

# response = requests.post(url, headers=headers, json=data)

# print("Status Code:", response.status_code)
# print("Response:", response.text)

import requests
import json
url = "https://history.mot.api.gov.uk/v1/trade/vehicles"



headers = {
    "Accept": "application/json+v6",
    "x-api-key": "B5fnZJm6F7axEdOZXaqGc8a5m6X6UqGT7yfRAU1B"
}

data = {
    "registrationNumber": "AB12CDE"
}

response = requests.post(url, headers=headers, json=data)
print(response)
with open('mot_data.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, indent=4)
print("Status Code:", response.status_code)
print("Response:", response.text)