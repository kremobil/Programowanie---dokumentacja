from re import T


t = 5, 11
x, y = t

print(x, y)

students_attendance = {"John": 96, "Adam": 80, "Dustin": 100}

print(list(students_attendance.items()))

for data in students_attendance.items():
  print(data, f"data[0]: {data[0]}, data[1]: {data[1]}")

people = [("Bob", 42, "Enginier"),("Tom", 54, "Mechanic"),("Jeff", 66, "Programer")]

for name, age, proffesion in people:
  print(f"{name} has {age} years and he is {proffesion}")

person = ("Bob", 42, "Enginier")
# przyjęto że to nieużywana zmienna _
name, _, proffesion = person
print(name, proffesion)

head, *tail = [1, 2, 3, 4, 5, 6, 7, 8]
print(head, tail)
