name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name = "Rolf"

print(greeting)

greeting = "hello, {}"
with_name = greeting.format(name)

print(with_name)

name = "John"

print(with_name)