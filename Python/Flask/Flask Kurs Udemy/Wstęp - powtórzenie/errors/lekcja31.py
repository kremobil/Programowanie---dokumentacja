def divide(dividend: int, divisor: int) -> float:
  if divisor == 0:
    raise ZeroDivisionError('Divisor cant be zero')
  
  return dividend / divisor

grades = []

print("Welcome to average grade program.")
try:
  average = divide(sum(grades), len(grades))
except ZeroDivisionError as bob:
  print(bob)
  print("There is no grades available in list.")
else:
  print(f"the average grade is {average}.")
finally:
  print("this is last.")