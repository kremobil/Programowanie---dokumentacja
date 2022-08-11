from operator import itemgetter

def divide(dividend: int, divisor: int):
  if divisor == 0:
    raise ZeroDivisionError("Divisor cant be 0")

  return dividend / divisor

def calculate(*values, operator):
  return operator(*values)

def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
  raise RuntimeError(f"Could not find an element with the expected value")

result = calculate(20, 4, operator=divide)
print(result)

friends = [
  {'name': 'John', 'age': 18},
  {'name': 'Rick', 'age': 25},
  {'name': 'Bob', 'age': 34},
]

def get_friend_name(friend):
  return friend['name']

# print(search(friends, "Bob", get_friend_name))
print(search(friends, "Bob", itemgetter('name')))

