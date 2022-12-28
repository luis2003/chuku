# Python script for chuku

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def print_ethbtc_price(url):
    # Use a breakpoint in the code line below to debug your script.
    response = requests.get(url)
    json_data = response.json()
    for k in json_data:
        #if k['symbol'] == 'ETHBTC':
        if 'USDT' in k['symbol']:
            symbol = k['symbol']
            price = k['price']
            print(f'Symbol: {symbol} - Price: {price}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_url = 'https://api.binance.com/api/v3/ticker/price'
    print_ethbtc_price(api_url)