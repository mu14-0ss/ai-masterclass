people = [
    {"name": "James", "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra", "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi", "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]}
]

# 1. Build a list of all step counts above 10,000 from any person
# We need a "double loop" comprehension to go through each person AND each day
high_steps = [step for person in people for step in person["steps"] if step > 10000]

# 2. Build a list of names whose average steps for the week is above 9,000
active_people = [
    person["name"] 
    for person in people 
    if sum(person["steps"]) / len(person["steps"]) > 9000
]

print("Steps above 10000:", high_steps)
print("People averaging above 9000:", active_people)