class Student:
    def __init__(self, name):
        self.name = name
        self.scores = [100, 100, 100, 100, 100]

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name


# Input names for both students
name1 = input("Enter the name of the first student: ").strip()
name2 = input("Enter the name of the second student: ").strip()

student1 = Student(name1)
student2 = Student(name2)

print("\nStudent Information")
print("-------------------")
print(f"Name: {student1.name}\nScores: {' '.join(map(str, student1.scores))}")
print(f"\nName: {student2.name}\nScores: {' '.join(map(str, student2.scores))}")
print("\n--------COMPARISON RESULTS--------")

# Comparison results with updated labels
print(f"\nComparing {student1.name} and {student2.name}:")
print(f"- Are they equal? {'Yes' if student1 == student2 else 'No'}")
print(f"- Is {student1.name} less than {student2.name}? {'Yes' if student1 < student2 else 'No'}")
print(f"- Is {student1.name} greater than or equal to {student2.name}? {'Yes' if student1 >= student2 else 'No'}")
