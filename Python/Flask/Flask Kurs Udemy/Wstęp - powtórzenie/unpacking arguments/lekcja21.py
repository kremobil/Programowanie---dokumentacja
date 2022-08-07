def multiply(*args:int)->int:
  print(args)
  total = 1
  for arg in args:
    total *= arg
  print(total)

def add(x:int, y:int = 10) -> str:
  return x + y

def apply(*args:int, operator:str):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator specified"

nums = [4, 5]
othernums = {'x': 15, 'y': 25}

multiply(3, 4, 2)
print(add(*nums))
print(add(**othernums))
multiply(*nums)
print(apply(*nums, operator="*"))