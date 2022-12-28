# Python script for Chuku (notification for prices changes on Binance)
import requests
import time
from pprint import pprint


def get_prices_usdt(url):
    response = requests.get(url)
    json_data = response.json()
    return_list = []
    for item in json_data:
        if 'USDT' in item['symbol']:
            return_list.append(item)
    return return_list


def get_dict_prices_usdt(url):
    response = requests.get(url)
    json_data = response.json()
    return_dict = {}
    for item in json_data:
        if 'USDT' in item['symbol']:
            return_dict[item['symbol']] = float(item['price'])
    return return_dict


def get_higher_prices(dict1, dict2):
    result_dict = {}
    for key, value in dict1.items():
        if key in dict2 and dict2[key] > dict1[key]:
            result_dict[key] = dict2[key]
    return result_dict


if __name__ == '__main__':
    api_url = 'https://api.binance.com/api/v3/ticker/price'
    usdt_prices_a = get_dict_prices_usdt(api_url)

    while True:
        time.sleep(3)
        usdt_prices_b = get_dict_prices_usdt(api_url)
        result = get_higher_prices(usdt_prices_a, usdt_prices_b)
        pprint(result)
        print('---')
