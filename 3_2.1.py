scores = [70, 85, 90]
total = 0

for score in scores:
    total += score

average = total/ len(scores)
print("Total:", total)
print("Average:", round(average,1))