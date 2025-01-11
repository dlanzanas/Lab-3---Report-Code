import random
#Name of class
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = [100, 100, 100, 100, 100]  # Default scores for 5 subjects
        
    def __repr__(self):
        return f"Name: {self.name}\nScores: {' '.join(map(str, self.scores))}"

    def __lt__(self, other):
        return self.name < other.name

num_students = int(input("Enter the number of students: "))
students = []

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ").strip()
    students.append(Student(name))

print("\nShuffled list of Students:")
random.shuffle(students)
for student in students:
    print(student)

print("\nSorted list of Students:")
students.sort()
for student in students:
    print(student)

