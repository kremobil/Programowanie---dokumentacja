class Person:
  def __init__(self, name:str, age:int):
    self.name = name
    self.age = age

  def __str__(self):
    return f"im {self.name} and im {self.age} years old"

  def __repr__(self):
    return f"<Person '{self.name}' {self.age}>"

bob = Person("Bob", 24)
print(bob)