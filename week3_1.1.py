def day_report(steps, water, protocol):
    print("--- Daily Report ---")
    print(f"Steps: {steps}")
    print(f"Water: {water} glasses")
    print(f"Protocol: {protocol}")
    print()  # blank line for spacing

def hit_goal(steps):
    if steps >= 8000:
        return True
    else:
        return False
    # You can also write it shorter: return steps >= 8000

# Call both functions with 3 different sets of values
day_report(10000, 8, "Followed morning routine")
print("Goal hit:", hit_goal(10000))
print()

day_report(5000, 5, "Missed workout")
print("Goal hit:", hit_goal(5000))
print()

day_report(12000, 10, "Full discipline day")
print("Goal hit:", hit_goal(12000))