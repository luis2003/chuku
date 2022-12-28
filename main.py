# Python script for Chuku (notification for prices changes on Binance)
import requests


def get_prices_usdt(url):
    response = requests.get(url)
    json_data = response.json()
    return_list = []
    for item in json_data:
        if 'USDT' in item['symbol']:
            return_list.append(item)
    return return_list


if __name__ == '__main__':
    api_url = 'https://api.binance.com/api/v3/ticker/price'
    usdt_prices = get_prices_usdt(api_url)
    for item in usdt_prices:
        symbol = item['symbol']
        price = item['price']
        print(f'Symbol: {symbol} - Price: {price}')
