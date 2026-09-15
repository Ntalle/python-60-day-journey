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
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("Where would you like to go? Left OR Right? ")

if direction.lower() == "left":
    Swim_or_wait = input("You came across a vast open ocean. You want to Wait or would you Swim? ")
    if Swim_or_wait.lower() == "wait":
        doors = input("Suddenly 3 doors appear to your right. \nYou can choose only one, choose wisely. Red, Blue or Yellow. ")
        if doors.lower() == "red":
            print("You are dead")
        elif doors.lower() == "yellow":
            print("You won the treasure. NOW SHARE IT WITH ME!!")
        elif doors.lower() == "blue":
            print("You sneeze your guts out")
        else:
            print("Wrong input. Try again")
    elif Swim_or_wait.lower() == "swim":
        print("You die horribily by a noble shark")
    else:
        print("Try agiain. Wrong input")
elif direction.lower() == "right":
    print("You die to your sins")
else:
    print("Wrong input try again")
