
import requests


currency_from = str(input("Enter currency converting from")).upper()
currency_to = str(input("Enter currency converting to")).upper()
amount = float(input("Enter amount to be converted"))



url = requests.get(f'http://api.exchangerate.host/convert?access_key=0b39e76fdf15c90ece4e1736d13383cd&from={currency_from}&to={currency_to}&amount={amount}')
valid_currency_codes = requests.get('http://api.exchangerate.host/list?access_key=0b39e76fdf15c90ece4e1736d13383cd')


# print( url.json()['result'])
all_currencies = valid_currency_codes.json()['currencies']
if currency_from not in all_currencies:
     raise KeyError(" from currency not in database")
elif currency_to not in all_currencies:
    raise KeyError(" to currency not in database")

else: print((url.json()['result']))
