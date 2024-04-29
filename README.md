# Telegram Name Updater

Automatically updates your Telegram last name with the current BTC/USDT price from Binance every 5 minutes.

## Requirements

- Python 3.9+
- Telegram API credentials ([my.telegram.org](https://my.telegram.org))

## Setup

1. Copy `src/config.json.example` to `src/config.json` and fill in your credentials:

```json
{
    "api_id": "YOUR_APP_API_ID",
    "api_hash": "YOUR_APP_API_HASH",
    "name_prefix": "Your Prefix ",
    "symbol": "BTCUSDT"
}
```

| Field | Description |
|---|---|
| `api_id` | Telegram API ID from my.telegram.org |
| `api_hash` | Telegram API hash from my.telegram.org |
| `name_prefix` | Text prepended before the price in your last name |
| `symbol` | Binance trading pair symbol (default: `BTCUSDT`) |

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
cd src && python main.py
```

On first run, you will be prompted to log in to your Telegram account. A session file (`tg_name_updater.session`) will be created for subsequent runs.

## Docker

```bash
docker compose up -d
```

The container will restart automatically on failure (up to 3 times).
