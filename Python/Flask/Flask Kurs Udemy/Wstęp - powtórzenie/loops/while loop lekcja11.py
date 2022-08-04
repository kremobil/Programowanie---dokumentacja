number = 7

while True:
  user_input = input("Would you like to play? (Y/n): ").lower()

  if user_input == "n":
    break
  
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

  
