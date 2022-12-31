from chuku import get_dict_prices_usdt, get_higher_percentage_prices

api_url = 'https://api.binance.com/api/v3/ticker/price'


def test_get_dict_prices_usdt():
    result = get_dict_prices_usdt(api_url)
    assert isinstance(result, dict)


def test_get_higher_percentage_prices_zero_price():
    percentage = 200
    dict1 = {'a': 1, 'b': 1, 'c': 1}
    dict2 = {'a': 1, 'b': 2, 'c': 1}
    result = get_higher_percentage_prices(dict1, dict2, percentage)
    assert isinstance(result, dict)
    assert len(result) == 0


def test_get_higher_percentage_prices_zero_price():
    percentage = 100
    dict1 = {'a': 1, 'b': 1, 'c': 1}
    dict2 = {'a': 1, 'b': 2, 'c': 1}
    result = get_higher_percentage_prices(dict1, dict2, percentage)
    assert isinstance(result, dict)
    assert len(result) == 1
