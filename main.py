# Python script for Chuku (notification for prices changes on Binance)
import requests


def get_prices_usdt(url):
    response = requests.get(url)
    json_data = response.json()
    return_list = []
    for k in json_data:
        if 'USDT' in k['symbol']:
            '''symbol = k['symbol']
            price = k['price']
            print(f'Symbol: {symbol} - Price: {price}')'''
            return_list.append(k)
    return return_list


if __name__ == '__main__':
    api_url = 'https://api.binance.com/api/v3/ticker/price'
    get_prices_usdt(api_url)
