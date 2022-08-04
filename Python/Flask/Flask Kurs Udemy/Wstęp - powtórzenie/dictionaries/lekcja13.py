friends_age = {"Bob": 24, "Adam": 25, "John": 26}
friends_age["Hoper"] = 34
friends_age["Bob"] = 31
print(friends_age)

friends = [
  {"name": "John", "age": 34},
  {"name": "Jane", "age": 16},
  {"name": "Jake", "age": 24}
]

for friend in friends:
  print(f"{friend['name']} has {friend['age']} years")

students_attendance = {"John": 96, "Adam": 80, "Dustin": 100}

for student, attendence in students_attendance.items():
  print(f"{student}: {attendence}%")

if "Bob" in students_attendance:
  print(f"Bob: {students_attendance['Bob']}")
else:
  print("Bob is not a student")

students_values = students_attendance.values()
print(sum(students_values) / len(students_values))