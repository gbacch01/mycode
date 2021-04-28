#!/usr/bin/env python3




#quiz = [{"Pick a Food":["Cheeseburger","Salad", "Pasta"]}, {"Pick a drink":["Soda", "Tea", "Coffee", "Water"]}]

#for question in quiz:
#    for x in question.keys():
#        print(x)
#answer1 = " "
#round = 0
while True:
    print("Do you like Cheese burger or Salad?")
    answer1 = input(">").lower()
    if answer1 == "cheese burger":
        health = 0
    elif answer1 == "salad":
       health = 1
       print("Do you like Tea or Soda?")
       answer2 = input(">").lower()
    if answer2 == "Tea":
       health2 = 1
    elif answer2 == "soda":
       health2 = 0



    if (health + health2) > 1:
       print("You are a picky eater")
    else:
       print("You are not a picky eater")



