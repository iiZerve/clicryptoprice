import requests
import argparse

def get_crypto_price(token):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data.get(token, {}).get("usd")

def main():
    parser = argparse.ArgumentParser(description="Get current price of a crypto token.")
    parser.add_argument("token", help="Crypto token symbol (e.g., bitcoin)")
    args = parser.parse_args()

    price = get_crypto_price(args.token)
    if price is not None:
        print(f"Current price of {args.token.upper()}: ${price}")
    else:
        print(f"Could not retrieve price for {args.token.upper()}")

if __name__ == "__main__":
    main()
