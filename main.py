# Python script for Chuku (notification for prices changes on Binance)
import requests
import time


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
    usdt_prices_a = get_prices_usdt(api_url)
    ''' # PRINTING LOGIC
    for item in usdt_prices:
        symbol = item['symbol']
        price = item['price']
        print(f'Symbol: {symbol} - Price: {price}')
    '''
    while True:
        time.sleep(3)
        usdt_prices_b = get_prices_usdt(api_url)
        # compare logic
        for item_a in usdt_prices_a:
            for item_b in usdt_prices_b:
                if item_a['symbol'] == item_b['symbol'] and item_a['price'] < item_b['price']:
                    symbol = item_a['symbol']
                    price = item_a['price']
                    higher_price = item_b['price']
                    print(f'Symbol: {symbol} - Price: {price} - Higher Price: {higher_price}')
        print('-----')
