daily_steps = {"mon": 9200, "tue": 7400, "wed": 10500, "thu":8800 }
print ("monday steps:", daily_steps["mon"])

daily_steps["fri"] = 11000
daily_steps["sat"] = 6900
daily_steps["sun"] = 9500
print ("---full week report---")
count = 0
for day, steps in daily_steps.items():
    if steps >=8000:
            print(day,":", steps, "-goal hit")
            count = count +1
    else:
            print(day,":", steps, "-below goal" )
print("total days over 8000:",count)
