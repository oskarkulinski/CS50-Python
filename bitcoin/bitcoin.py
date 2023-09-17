import sys
import requests

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    ...
except requests.RequestException:
    ...