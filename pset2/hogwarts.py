students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# students = ["Hermoine", "Harry", "Ron"]
for student in students:
    print(student)

# students = ["Hermoine", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])


# using a dict to associate keys with values
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")

# Have lots of data associated multiple things
# list of dicts created
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
#for loop iterate through each of the dict's inside the list called students
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")