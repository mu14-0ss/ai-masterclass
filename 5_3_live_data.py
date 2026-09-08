import requests
import json
from datetime import datetime

# 1. CONFIGURATION
BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = "bitcoin,ethereum,solana"
CURRENCY = "usd"
OUTPUT_FILE = "crypto_prices.json"

# 2. FETCH FUNCTION
def fetch_crypto_prices():
    """Fetch live prices from CoinGecko API"""
    params = {
        "ids": COINS,
        "vs_currencies": CURRENCY
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# 3. PROCESS FUNCTION
def process_data(raw_data):
    """Transform raw API data into a clean list of dicts"""
    if raw_data is None:
         return []
    
    processed = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for coin, price_data in raw_data.items():
        processed.append({
            "coin": coin,
            "price_usd": price_data[CURRENCY],
            "timestamp": timestamp
        })
    
    return processed

# 4. OUTPUT FUNCTION
def save_to_json(data):
    """Save processed data to a JSON file"""
    try:
        with open(OUTPUT_FILE, "w") as f:
            json.dump(data, f, indent=4)  # indent=4 makes it pretty
        print(f"Data saved successfully to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving data: {e}")

        # WIRE IT ALL TOGETHER
def main():
    print("Fetching crypto prices...")
    raw = fetch_crypto_prices()
    
    print("Processing data...")
    clean = process_data(raw)
    
    print("Saving to file...")
    save_to_json(clean)

    display_prices(clean)

    # 5. READ AND DISPLAY FUNCTION
def display_prices(data):
    """Print prices nicely in terminal"""
    print("\n=== LIVE CRYPTO PRICES ===")
    for item in data:
        print(f"{item['coin'].upper()}: ${item['price_usd']}")
    print(f"Last updated: {data[0]['timestamp']}")
    print("==========================")




# This makes sure main() runs when you run the file
# if__name__=="__main__"
main()