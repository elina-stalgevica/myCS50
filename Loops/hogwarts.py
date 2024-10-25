#for loop - for creates a variable for you. Most popular - i

students = ["Hermione", "Harry", "Ron", "Draco"]

# How to print each student seperately
for student in students:
    print(student)

# Another option (len - length)
# You can add i before students[i] - to see position in list
for i in range(len(students)):
    print(i, students[i])

#dict - dictionaries , allows to assiciate one value with another. Curly braces.
# Single dicionarie
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",}

# Access to student and the house
for student in students:
    print(student, students[student], sep=", ")

# A bigger dicitionarie
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
