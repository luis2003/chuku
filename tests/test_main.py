from main import get_prices_usdt


def test_get_prices_usdt():
    api_url = 'https://api.binance.com/api/v3/ticker/price'
    result = get_prices_usdt(api_url)
    assert isinstance(result, list)
