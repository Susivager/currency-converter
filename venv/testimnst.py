import requests
import json

url = "https://api.apilayer.com/currency_data/list"

payload = {}
headers= {
  "apikey": "mU6bap1imPwGt4R9RU6xwXwDHg1EFVYn"
}

response = requests.request("GET", url, headers=headers, data=payload)
status_code = response.status_code
resultrequest = response.text
result = json.loads(resultrequest)
print(result)
print(status_code)