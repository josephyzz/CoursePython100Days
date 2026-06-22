import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {
    student: score
    for (student, score) in students_scores.items()
    if score >= 60
}

### 200. How to interate  over a panda Dataframe
import pandas

student_dict = {'student': ['Angela', 'James', 'Lily'], 'score': [56, 76, 98]}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for key, value in student_data_frame.items():
#    print(value)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    print(row)
