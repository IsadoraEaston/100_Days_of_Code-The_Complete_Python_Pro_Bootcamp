print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure island.")
Answer1 = input("Do you want to go left or right? Type 'left' or 'right': ")
if Answer1 == "left":
    Answer2 = input(print("You arrived at a lake. Do you want to wait for the boat or swim? Type 'swim' or 'wait': "))
    if Answer2 == "wait":
        Answer3 = input("You reached the island unharmed."
        "There is a house with 3 doors : Red, Yellow, Blue."
        "Which one do you choose to open? R for red, Y for yellow, B for blue")
        if Answer3 == "R":
            print("GAME OVER. You are burned by a  fire.")
        elif Answer3 == "B":
            print("GAME OVER. You are eaten by a beast.")
        elif Answer3 == "Y":
            print("YOU WIN. You found the treasure!!")
    else:
        print("GAME OVER. You got attacked by a crocodile.")
else:
    print("GAME OVER. You fell into a hole.")




