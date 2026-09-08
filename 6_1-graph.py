import pandas as pd
import matplotlib.pyplot as plt

# Read your CSV
df = pd.read_csv('crypto_prices.csv')

# Convert timestamp to real datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Make a chart for each coin
plt.figure(figsize=(12,6))
for coin in df['Coin'].unique():
    coin_data = df[df['Coin'] == coin]
    plt.plot(coin_data['Timestamp'], coin_data['Price_USD'], label=coin)

plt.title('Crypto Prices Over Time')
plt.xlabel('Time')
plt.ylabel('Price USD')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()