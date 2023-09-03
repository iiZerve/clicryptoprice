import requests
import argparse

# A mapping of symbol tickers to full names
symbol_to_name = {
    "btc": "bitcoin",
    "eth": "ethereum",
    # Add more mappings as needed
}

def get_full_name(input_token):
    # Check if the input is a valid symbol ticker, and return the corresponding full name
    return symbol_to_name.get(input_token.lower())

def get_crypto_price_on_exchange(token, exchange):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": token,
        "vs_currencies": "usd",
    }

    response = requests.get(url, params=params)
    data = response.json()

    if token in data and "usd" in data[token]:
        price = data[token]["usd"]
        return price
    else:
        return None

def main():
    parser = argparse.ArgumentParser(description="Get current price of a crypto token on multiple exchanges.")
    parser.add_argument("token", help="Crypto token symbol or full name (e.g., ethereum or eth)")
    parser.add_argument("--exchanges", nargs='*', default=['coingecko'], help="List of exchange names separated by space (e.g., coingecko binance coinbase)")
    args = parser.parse_args()

    input_token = args.token.lower()  # Convert input token to lowercase

    # Check if the input token is a valid symbol ticker, and get its corresponding full name
    full_name = get_full_name(input_token) if input_token in symbol_to_name else input_token

    for exchange in args.exchanges:
        exchange = exchange.lower()  # Convert exchange name to lowercase
        price = get_crypto_price_on_exchange(full_name, exchange)

        if price is not None:
            print(f"{full_name.capitalize()} ({exchange.capitalize()}): ${price:.2f}")
        else:
            print(f"Could not retrieve price for {full_name.capitalize()} on {exchange.capitalize()}")

if __name__ == "__main__":
    main()
