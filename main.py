import os
from datetime import datetime

from dotenv import load_dotenv
from lemon import api


load_dotenv()
client = api.create(
    trading_api_token=os.environ.get('TRADING_API_KEY'),
    market_data_api_token=os.environ.get('DATA_API_KEY'),
    env='paper'
)
print(client)


def demo_data():
    # get venues
    response = client.market_data.venues.get()
    print(response.results)

    # get instruments
    response = client.market_data.instruments.get(
        isin=["US88160R1014", "US0231351067"]
    )
    print(response.results)

    response = client.market_data.instruments.get(
        type=['stock', 'etf'],
        currency=['EUR'],
        limit=10,
        sorting='asc'
    )
    print(response.results)


def demo_trading():

    # activate buy order
    response = client.trading.orders.create(
        isin='US88160R1014',
        side='buy',
        quantity=1,
        venue='xmun'
    )
    order_id = response.results.id
    print(response.results)
    response = client.trading.orders.activate(order_id=order_id)
    print(response)

    # get buy order status
    response = client.trading.orders.get_order(order_id=order_id)
    print(response.results)

    # cancel order
    response = client.trading.orders.create(isin='US88160R1014', side='buy', quantity=1, venue='xmun')
    print(response.results)
    response = client.trading.orders.cancel(order_id=response.results.id)
    print(response)


if __name__ == '__main__':
    demo_data()
    # demo_trading()
