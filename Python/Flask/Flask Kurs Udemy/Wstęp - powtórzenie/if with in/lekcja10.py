from tkinter import N


movies_watched = {"the matrix", "green book", "harry potter"}
user_movie = input("Enter something you watched recently:").lower()

if user_movie in movies_watched:
  print(f"I've watched {user_movie} too!")
else:
  print(f"I haven't watched {user_movie} yet!")

number = 7
user_input = input("If you want to play enter 'y': ").lower()

if user_input == "y":
  user_number = int(input("guess our number"))
  if user_number == number:
    print("You guess correctly")
  # elif number - user_number in (1, -1):
  #   print("you were off by one")
  
  # abs zamienia na liczbę dodatnią naprzykład -1 na 1 albo -10 na 10
  elif abs(number - user_number) == 1:
    print("you were off by one")
  else:
    print("Maybe you guess next time?")

