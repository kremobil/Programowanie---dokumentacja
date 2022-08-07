add = lambda x, y: x + y
print((lambda x, y: x + y)(5, 7))

print(add(4, 6))

def double(x:int)-> int:
  return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = list(map(double, sequence))