import random
import math

total = 0

for i in range(1, 6):
    roll = random.randint(1, 6)
    print(f"Roll {i}: {roll}")
    total += roll

average = total / 5
average_floor = math.floor(average)

print(f"\nTotal: {total}")
print(f"Average rounded down: {average_floor}")
print("\n--- Price Discount ---")

price = random.randint(1500, 5000)  # random price
discounted = price * 0.85  # 15% off
discounted_ceil = math.ceil(discounted)  # round UP

print(f"Original: {price}")
print(f"Discounted: {discounted_ceil}")
print("\n--- Study Hours ---")

total_hours = 0
for day in range(1, 8):  # 1 to 7 days
    hours = random.randint(1, 8)  # 1 to 8 hours per day
    print(f"Day {day}: {hours} hours")
    total_hours += hours

avg_hours = total_hours / 7
avg_floor = math.floor(avg_hours)

print(f"\nTotal hours: {total_hours}")
print(f"Average rounded down: {avg_floor} hours/day")