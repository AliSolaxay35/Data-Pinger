import requests

# Simple price endpoint
url_simple = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
res_simple = requests.get(url_simple)

print("Checking simple price:")
print("Response:", res_simple)  # <Response [200]>
print("Status Code:", res_simple.status_code)

if res_simple.status_code == 200:
    simple_price = res_simple.json()
    print("Simple Price (USD):", simple_price['bitcoin']['usd'])
else:
    print("Failed to fetch simple price")

print("\nFetching market data...")

# Market data endpoint
url_market = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
res_market = requests.get(url_market)

if res_market.status_code == 200:
    data = res_market.json()
    if isinstance(data, list) and len(data) > 0:
        price = data[0]
        print("Coin:", price['name'])
        print("Current Price:", price['current_price'], "USD")
        print("High 24h:", price['high_24h'], "USD")
        print("Low 24h:", price['low_24h'], "USD")
        print("24h Change (%):", price['price_change_percentage_24h'], "%")
    else:
        print("Market data not found.")
else:
    print("Market request failed:", res_market.status_code)
