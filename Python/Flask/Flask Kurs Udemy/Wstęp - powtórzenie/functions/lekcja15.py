def hello():
  print("Hello!")

def user_age_in_seconds():
  user_age = int(input("Enter your age: "))
  age_secounds = user_age * 365 * 24 * 60 * 60
  print(f"Your age in secounds is {age_secounds} sec")

hello()
user_age_in_seconds()