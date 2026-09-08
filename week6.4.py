import numpy as np

# Think: 3 students, 3 subjects
grades = np.array([
    [80, 85, 90], # Student 1: Math, English, Science
    [70, 75, 80], # Student 2
    [90, 95, 100] # Student 3
])

print(grades)
print(grades[1]) # Should print Student 2's scores
print(grades[:, 2]) # Should print all Science scores 
print(grades.mean()) # Should print class average
student_averages = grades.mean(axis=1) # average of each ROW
print(student_averages) # What do you think this prints?
print(student_averages[student_averages > 85]) # Who passed?