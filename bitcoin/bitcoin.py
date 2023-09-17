import sys
import requests
import json

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Request unsuccessful")

rate = (info.json()["bpi"]["USD"]["rate"])
price = rate * n
print(f"${price:,.4f}")