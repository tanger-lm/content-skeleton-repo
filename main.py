import os
from datetime import datetime

from dotenv import load_dotenv
from lemon import api

load_dotenv()

# create your client
client = api.create(
    trading_api_token=os.environ.get('TRADING_API_KEY'),
    market_data_api_token=os.environ.get('DATA_API_KEY'),
    env='paper'  # or 'money'
)


def demo_venue():
    # get venues
    response = client.market_data.venues.get()
    print(response.results)
    print('\n')


def demo_account():
    # get account details
    response = client.trading.account.get()
    print(response.results)


def demo_activate():
    # activate buy order
    response = client.trading.orders.create(isin='US88160R1014', side='buy', quantity=1, venue=os.getenv('MIC'))
    order_id = response.results.id
    print(response.results)
    response = client.trading.orders.activate(order_id=order_id)
    print(response)


def demo_cancel():
    # cancel order
    response = client.trading.orders.create(
        isin='US88160R1014',
        side='buy',
        quantity=1,
        venue=os.getenv('MIC'),
        stop_price=6810000,
        limit_price=6850000,
        expires_at=datetime(2022, 7, 1)
    )
    order_id = response.results.id
    print(response.results)
    response = client.trading.orders.cancel(order_id=order_id)
    print(response)


if __name__ == '__main__':
    demo_venue()
    demo_account()
    demo_activate()
    demo_cancel()
