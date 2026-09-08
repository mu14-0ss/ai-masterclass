import requests
import time

coins = "bitcoin,ethereum,solana"

while True:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coins}&vs_currencies=usd&include_24hr_change=true"
    data = requests.get(url).json()

    print("\n--- LIVE CRYPTO PRICES ---")
    for coin in coins.split(","):
        price = data[coin]['usd']
        change = data[coin]['usd_24h_change']
        print(f"{coin.upper()}: ${price:,.2f} | 24h: {change:+.2f}%")

    time.sleep(10) # wait 10 seconds then refresh
    import requests
import time
import csv
import os
from datetime import datetime

def get_prices(coins):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coins}&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url)
    return response.json()

def save_to_csv(filename, timestamp, coin_data):
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write header only first time
        if not file_exists:
            writer.writerow(['Timestamp', 'Coin', 'Price_USD', 'Change_24h'])
        
        for coin, data in coin_data.items():
            writer.writerow([timestamp, coin.upper(), data['usd'], data['usd_24h_change']])

def main():
    filename = "crypto_prices.csv"
    coins = "bitcoin,ethereum,solana"
    
    print("=== CRYPTO CSV TRACKER ===")
    print(f"Saving data to: {filename}")
    print("Press Ctrl + C to stop\n")

    try:
        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = get_prices(coins)
            
            print(f"--- {timestamp} ---")
            for coin in coins.split(","):
                if coin in data:
                    price = data[coin]['usd']
                    change = data[coin]['usd_24h_change']
                    emoji = "📈" if change > 0 else "📉"
                    print(f"{emoji} {coin.upper():10} ${price:,.2f} | 24h: {change:+.2f}%")
            
            save_to_csv(filename, timestamp, data)
            print(f"Data saved to {filename}\n")
            
            time.sleep(10)

    except KeyboardInterrupt:
        print("\n\nTracker stopped. Check your crypto_prices.csv file 💰")

if _name_ == "_main_":
    main()