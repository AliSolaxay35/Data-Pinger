import requests

my_good_price = 45000

response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
price = float(response.json()['bitcoin']['usd'])

print(f'Bitcoin price is currently {int(price)} USD.')

if price < my_good_price:
    print("inform AS35WLT")  