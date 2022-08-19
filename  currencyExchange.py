import requests
import json
import os


os.system('clear')
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
data = data['Valute']

print("Please, select currency code to compare with RUB:")


for key in data:
    print(key)


currency_code = input('Type currency code here: ')

current_currency = data[currency_code]

print('1' + currency_code + " = " + str(current_currency['Value']) + "RUB")

