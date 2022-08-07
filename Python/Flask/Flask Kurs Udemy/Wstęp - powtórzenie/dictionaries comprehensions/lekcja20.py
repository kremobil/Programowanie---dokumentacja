users = [
  (0, "Bob", "password"),
  (1, "Rick", "bob123"),
  (2, "Jose", "longp4a$$w0rd"),
  (3, "John", "123456789")
]

username_mapping= {user[1]: user for user in users}

print(username_mapping)

username_input = input("Enter your name: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
  print("you loged correctly")
else:
  print("details are wrong")