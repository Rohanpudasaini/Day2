import sys
import requests
lists = sys.argv
if len(list) < 2:
    sys.exit("Missing command-line argument")
try:
    number = float(lists[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
# print(lists)
# print(type(number))

try:
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.exceptions:
    print("Exception in Requests")
    sys.exit()
json1 = res.json()
rate = json1["bpi"]["USD"]["rate_float"]
# print(rate)
final_cost = rate * number
print(f"{final_cost:,.4f}")
