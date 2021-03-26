from bybit import *
from os import environ

client = bybit(test=False, api_key=environ.get('API_KEY'), api_secret=environ.get('API_SECRET'))


def timestamp():
    return client.Common.Common_getTime().result()[0].get('time_now')


def wallet_balance():
    return client.Wallet.Wallet_getBalance(coin="BTC", timestamp=timestamp()).result()[0].get('result').get('BTC').get(
        'available_balance')


def leverage():
    return client.Positions.Positions_myPosition(symbol="BTCUSD", timestamp=timestamp()).result()[0].get('result').get(
        'leverage')


def last_price():
    return client.Market.Market_symbolInfo(symbol='BTCUSD').result()[0].get('result')[0].get('last_price')


def position():
    response = client.Positions.Positions_myPosition(symbol="BTCUSD", timestamp=timestamp()).result()[0].get('result')
    return response


def position_size():
    return 0


def post_trade():
    return client.Order.Order_new(side="Buy", symbol="BTCUSD", timestamp=timestamp(), order_type="Limit", qty=0,
                                  price=0, time_in_force="GoodTillCancel").result()[0]


def close_trade():
    return client.Order.Order_new(side="Sell", symbol="BTCUSD", order_type="Limit", qty=position_size(),
                                  price=last_price(), timestamp=timestamp(), time_in_force="GoodTillCancel").result()[0]
