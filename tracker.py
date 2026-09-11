import requests
import json
import time
from datetime import datetime

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = "bitcoin,ethereum,solana,cardano"
CURRENCY = "usd"

def fetch_crypto_prices():
    params = {
        "ids": COINS,
        "vs_currencies": CURRENCY,
        "include_24hr_change": "true"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_data(raw_data):
    processed = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for coin, data in raw_data.items():
        processed.append({
            "coin": coin.upper(),
            "price_usd": data[CURRENCY],
            "change_24h": round(data.get(f"{CURRENCY}_24h_change", 0), 2),
            "timestamp": timestamp
        })
    return processed

def display_prices(data):
    print("\n--- LIVE CRYPTO PRICES ---")
    for item in data:
        arrow = "📈" if item['change_24h'] >= 0 else "📉"
        print(f"{arrow} {item['coin']}: ${item['price_usd']} ({item['change_24h']}%)")
    print(f"Last updated: {data[0]['timestamp']}")

def save_to_json(data, filename="crypto_prices.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    print("Starting Live Tracker... Ctrl+C to stop")
    while True:
        raw = fetch_crypto_prices()
        if raw:
            clean = process_data(raw)
            display_prices(clean)
            save_to_json(clean)
        print("Waiting 10s...\n")
        time.sleep(10)

if __name__ == "__main__":
    main()