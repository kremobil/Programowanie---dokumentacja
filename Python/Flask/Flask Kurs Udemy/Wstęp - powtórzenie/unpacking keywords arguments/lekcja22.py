def named(**kwargs):
  print(kwargs)



def namedrevers(name, age):
  print(name, age)

def both(*args, **kwargs):
  print(args, kwargs)

details = {"name": "Bob", "age": 25}

named(name="Bob", age="25")
namedrevers(**details)
both(1,3,"hey", name="Bob", age="25")