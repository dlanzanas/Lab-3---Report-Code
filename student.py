class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name
name1 = input("Enter the name of the first student: ").strip()
name2 = input("Enter the name of the second student: ").strip()

scores1 = []
scores2 = []

student1 = Student(name1, scores1)
student2 = Student(name2, scores2)

print("\n--------STUDENT DETAILS--------")
print(f"\nName: {student1.name}\nScores: {' '.join(map(str, student1.scores))}")
print(f"\nName: {student2.name}\nScores: {' '.join(map(str, student2.scores))}")
print("\n--------COMPARISON RESULTS--------")

print(f"\nComparing {student1.name} and {student2.name}:")
print(f"- Are they equal? {'Yes' if student1 == student2 else 'No'}")
print(f"- Is {student1.name} less than {student2.name}? {'Yes' if student1 < student2 else 'No'}")
