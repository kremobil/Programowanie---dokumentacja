numbers = [1,2,3,4,5,6,7,8,9]
doubled = [x * 2 for x in numbers]

print(doubled)

friends = ["Sam", "Tom", "Samantha", "Simon", "Bob"]
start_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(start_s)
print(friends is start_s)
print("friends: ", id(friends), "start_s: ", id(start_s))