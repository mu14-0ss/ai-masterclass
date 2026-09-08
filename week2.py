week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

print("---weekly step check---)

for steps in week_steps:
    if steps >=8000:
     print(steps, "-goal hit)
     else:
      print(steps, "-below goal")

      print("days tracked:", len(week_steps))