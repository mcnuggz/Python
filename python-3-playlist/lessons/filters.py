grades = ['A', 'B', 'C', 'F', 'F', 'A']
#filter(function, data)

def remove_failingGrades(grade):
    return grade != 'F'


print(list(filter(remove_failingGrades, grades)))

filtered_grades = []
for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)

print(filtered_grades)

#comprehension
print([grade for grade in grades if grade != 'F'])