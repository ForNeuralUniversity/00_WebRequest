import requests
import json
#https://www.tutorialspoint.com/how-to-clear-python-shell
import os
os.system('clear')


url = 'https://www.cbr-xml-daily.ru/daily_json.js'
# почитать - https://www.cbr-xml-daily.ru/
response = requests.get(url)
print(response)

data = json.loads(response.text)
for key in data.keys():
    print(key)
print()

data = data['Valute']
for key in data.keys():
    print(key)
print()

data = data['USD']
for key in data.keys():
    print(key)
    print(data[key])