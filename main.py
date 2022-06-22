import os
from datetime import datetime

from dotenv import load_dotenv
from lemon import api

load_dotenv()
client = api.create(
    trading_api_token=os.environ.get('TRADING_API_KEY'),
    market_data_api_token=os.environ.get('DATA_API_KEY'),
    env='paper'  # or 'money'
)
print(client)


def demo_data():
    # get venues
    response = client.market_data.venues.get()
    print(response.results)
    print('\n')


def demo_trading():
    # activate buy order
    response = client.trading.account.get()
    print(response.results)


if __name__ == '__main__':
    demo_data()
    demo_trading()
