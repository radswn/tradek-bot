from requests import get
from os import environ


def get_macd_histogram():
    secret_key = environ.get('INDICATOR_API_KEY_1')
    response = get(
        'https://api.taapi.io/macd?secret=' + secret_key + '&exchange=binance&symbol=BTC/USDT&interval=1h')
    return response.json().get['valueMACDHist']
