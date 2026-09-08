me = {"name": "Eric", "city": "nairobi", "age": 27}

# 1. Loop through keys
for key in me:
    print(key)  # name, city, age

# 2. Loop through values
for value in me.values():
    print(value)  # Eric, nairobi, 27

# 3. Loop through key AND value
for key, value in me.items():
    print(key, ":", value)