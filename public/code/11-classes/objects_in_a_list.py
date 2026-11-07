# Unit 11 — many objects in a list
# Run this with the Run button in your editor.

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    # A method can call another method of the same object with self.
    def report(self):
        return f"{self.name}: {self.average():.1f}"


ada = Student("Ada")
grace = Student("Grace")
alan = Student("Alan")

ada.add_score(88)
ada.add_score(92)
grace.add_score(95)
grace.add_score(98)
alan.add_score(71)

# Each object keeps its own list. Ada's scores are not Grace's scores.
print(ada.scores)            # [88, 92]
print(grace.scores)          # [95, 98]

print()

# ---------------------------------------------------------------
# A list of objects works like any other list.
students = [ada, grace, alan]

for student in students:
    print(student.report())

print()

# The "best so far" pattern from unit 04, with objects.
best = students[0]
for student in students:
    if student.average() > best.average():
        best = student
print(f"Best: {best.name}")

print()

# ---------------------------------------------------------------
# Finding one object by name. Give back the object, or None.

def find_student(students, name):
    for student in students:
        if student.name.lower() == name.lower():
            return student
    return None

found = find_student(students, "grace")
if found is None:
    print("No such student")
else:
    print(f"Found {found.name}, scores {found.scores}")

print(find_student(students, "Linus"))   # None

print()

# Printing the whole list shows the ugly form for each object.
# Loop over it instead, as above.
print(students[0])           # <__main__.Student object at 0x...>
