steps = [8800, 6500, 11000, 9200, 7300]
steps.append (10500)
steps.remove(6500)
steps.sort(reverse=True)

print("final list:", steps)
average =0
for s in steps:
    if s > 10000:
        average = average + 1
print("days over 10000:", average)