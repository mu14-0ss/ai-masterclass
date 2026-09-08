import numpy as np

py_list = [10, 20, 30]
np_array = np.array([10, 20, 30])

print(py_list * 2)   # What happens?
print(np_array * 2)  # What happens?

import numpy as np

print(np.zeros(4)) # 4 zeros
print(np.ones(3)) # 3 ones 
print(np.arange(0, 10)) # 0 to 9

scores = np.array([50, 60, 70, 80])

print(scores + 10)   # Teacher adds 10 bonus marks
print(scores * 2)    # Double everyone's score
print(scores.mean()) # What's the class average?


print(scores[scores > 70])  # Get only scores above 70
print(scores[scores < 65])  # Get only scores below 65