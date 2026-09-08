import json

week_report = {
    "name": "Eric",
    "steps": [3000, 12500, 9000, 14000, 5400],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# 1. Convert dict to JSON string
json_string = json.dumps(week_report, indent=4)
print("JSON String:")
print(json_string)

# 2. Load it back to Python dict
loaded_report = json.loads(json_string)

# 3. Compute average steps
steps_list = loaded_report["steps"]
average_steps = sum(steps_list) / len(steps_list)

print("\nAverage steps:", average_steps)

print("\nFile saved! check your Desktop/A.I masterrclass folder for eric_week1.json")