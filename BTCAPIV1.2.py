import requests

def inform_AS35WLT(price):
    print(f"inform AS35WLT: Bitcoin price dropped to {int(price)} USD!")

my_good_price = 200000

response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
price = float(response.json()['bitcoin']['usd'])

print(f"Bitcoin price is currently {int(price)} USD.")

if price < my_good_price:
    inform_AS35WLT(price) 
