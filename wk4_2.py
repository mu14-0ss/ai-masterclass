while True:  # keep asking until they get it right
    try:
        steps = int(input("enter steps for today: " ))
        # If they type a number, we break out of the loop
        break
    except ValueError:
        print("Oops! Please enter a number like 8000, not text")
    else:  # runs ONLY if try worked
        print("Input accepted!")
    finally: # runs NO MATTER WHAT
        print("Thank you for using the step tracker")

if steps >= 8000:
    print(f"Great job! {steps} steps. Goal met!")
else:
    print(f"{steps} steps. Keep going!") 