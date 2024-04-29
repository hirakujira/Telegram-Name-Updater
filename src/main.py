from telethon import TelegramClient, types
from telethon.tl.functions.account import UpdateProfileRequest, UpdateBirthdayRequest
import asyncio
import json
import requests
import datetime

client = None
previous_day = None

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def start_client():
    global client
    config = load_config()
    client = TelegramClient('tg_name_updater', config['api_id'], config['api_hash'])
    client.start()

def get_price(symbol):
    url = f'https://api.binance.com/api/v3/avgPrice?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    price = format(float(data['price']), ',.0f')
    return price

async def main():
    config = load_config()
    symbol = config.get('symbol', 'BTCUSDT')
    async with client:
        while True:
            price = get_price(symbol)
            await client(UpdateProfileRequest(last_name=config['name_prefix'] + "$" + price))

            print("Updated name to: " + config['name_prefix'] + "$" + price)
            await asyncio.sleep(300)

start_client()
asyncio.get_event_loop().run_until_complete(main())
