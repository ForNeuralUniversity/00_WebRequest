import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
# почитать - https://www.cbr-xml-daily.ru/
response = requests.get(url)
data = json.loads(response.text)
print(response)
print(data)