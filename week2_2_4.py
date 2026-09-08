week_log = [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"},
]

# 1. Loop that prints each day's details
for entry in week_log:
    print(f"{entry['day']}: {entry['steps']} steps, Protocol: {entry['protocol']}")

# 2. Calculate and print average steps
total_steps = sum(entry["steps"] for entry in week_log)
average_steps = total_steps / len(week_log)

print(f"\nAverage steps: {average_steps:.0f}")