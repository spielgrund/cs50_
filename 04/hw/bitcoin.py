import json
import requests
import sys


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
else:
    try:
        btc_amount = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit()

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    btc_price = response["bpi"]["USD"]["rate_float"]
    total_amount = btc_price * btc_amount
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("requestexception")

