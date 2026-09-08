steps = [8800, 6500, 11000, 9200, 7300]

steps.append(10500)   
steps.remove(6500)    
steps.sort(reverse=True)

print("final list:", steps)

count = 0
total = 0

for s in steps:
    if s > 9000:
         count = count + 1
print("days over 9000:",count)