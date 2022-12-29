# Python script for Chuku (notification for prices changes on Binance)
import requests
import time
from mail import send_email


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


def get_higher_percentage_prices(dict1, dict2, percentage):
    result_dict = {}
    for key, value in dict1.items():
        if key in dict2:
            perc_diff = ((dict2[key]/dict1[key]) - 1) * 100
            if perc_diff >= percentage:
                result_dict[key] = dict2[key]
    return result_dict


if __name__ == '__main__':
    api_url = 'https://api.binance.com/api/v3/ticker/price'
    seconds = int(input('Ingresar SEGUNDOS (a esperar entre refresco de datos de Binance):'))
    percentage = float(input('Ingresar PORCENTAJE (de variacion minima del precio a monitorear):'))
    print('---(oprimir Crtl+C para parar el programa)---')
    usdt_prices_a = get_dict_prices_usdt(api_url)
    t = time.localtime()
    hist_date_time = time.strftime("%b/%d-%H:%M:%S", t)

    try:
        while True:
            time.sleep(seconds)
            usdt_prices_b = get_dict_prices_usdt(api_url)
            t = time.localtime()
            refresh_date_time = time.strftime("%b/%d-%H:%M:%S", t)
            result = get_higher_percentage_prices(usdt_prices_a, usdt_prices_b, percentage)
            mail_text = ''
            for key, value in result.items():
                symbol = key
                price = value
                prev_price = usdt_prices_a[key]
                perc_diff = round(((price / prev_price) - 1) * 100, 4)
                message = f'Nombre: {symbol} - Precio({refresh_date_time}): {price} - ' \
                          f'Precio Ant.({hist_date_time}): {prev_price} - ' \
                          f'Variacion: {perc_diff}\n%'
                print(message)
                mail_text += message
            if len(mail_text) > 1:
                send_email(mail_text)
            print('---(Oprimir Crtl+C para parar el programa)---')
    except KeyboardInterrupt:
        pass
