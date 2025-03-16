import requests
import sys


def main():

    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        bitcoin(sys.argv[1])
    except requests.RequestException:
        sys.exit()


def bitcoin(x):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    n = r.json()
    rate = float(n["bpi"]["USD"]["rate"].replace(",", ""))
    try:
        amount = rate * float(x)
        print(f"${amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")


main()
