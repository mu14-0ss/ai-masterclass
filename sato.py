import requests

# Put your REAL key here when ready
REAL_WEATHER_KEY = "PUT_REAL_KEY_HERE" 
FAKE_KEY = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

print("=== 3-API DASHBOARD ===")

# API 1: Weather - REAL
url1 = f"http://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid={REAL_WEATHER_KEY}&units=metric"
r1 = requests.get(url1)
print("API 1 Weather Status:", r1.status_code)

# API 2: News - FAKE
url2 = f"https://newsapi.org/v2/top-headlines?country=ke&apiKey={FAKE_KEY}"
r2 = requests.get(url2)
print("API 2 News Status:", r2.status_code)

# API 3: Currency - FAKE 
# API 3: Currency - REAL DATA!
url3 = "https://api.exchangerate-api.com/v4/latest/USD"
r3 = requests.get(url3)
data3 = r3.json()
print("API 3 Currency: 200 ✅")
print(f" 1 USD = {data3['rates']['KES']} KES")
print(f" 1 USD = {data3['rates']['EUR']} EUR")

if r1.status_code == 200:
    data1 = r1.json()
    temp = data1['main']['temp']
    print(f"API 1 weather: {temp}°C in nairobi")
else:
    print("API 1 weather: need real key") 

    print("=== 3-API DASHBOARD ===")
print(f"API 1 Weather: {temp}°C" if r1.status_code == 200 else "API 1 Weather: need real key")
print(f"API 2 News: {r2.status_code}") 
print(f"API 3 Currency: 1 USD = {data3['rates']['KES']} KES")

import requests
import time  # <-- new

FAKE_KEY = "a1b2c3d4e5f6g7h8i9j0k112m3n4o5p6"

while True:  # <-- this makes it loop forever
    # Clear the screen look
    print("\n" * 3)  
    print("=== 3-API DASHBOARD ===")
    
    # API 1: Weather
    url1 = f"https://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid={FAKE_KEY}&units=metric"
    r1 = requests.get(url1)
    
    # API 2: News - FAKE
    url2 = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={FAKE_KEY}"
    r2 = requests.get(url2)
    
    # API 3: Currency - REAL DATA
    url3 = "https://api.exchangerate-api.com/v4/latest/USD"
    r3 = requests.get(url3)
    data3 = r3.json()
    
    print(f"API 3 Currency: {r3.status_code} ✅")
    print(f"1 USD = {data3['rates']['KES']} KES")
    print(f"1 USD = {data3['rates']['EUR']} EUR")
    
    if r1.status_code == 200:
        data1 = r1.json()
        temp = data1['main']['temp']
        print(f"API 1 Weather: {temp}°C in nairobi")
    else:
        print("API 1 Weather: need real key")
    
    print(f"API 2 News: {r2.status_code}")
    
    print("\nRefreshing in 5 seconds...")
    time.sleep(5)  # wait 5 seconds then loop again