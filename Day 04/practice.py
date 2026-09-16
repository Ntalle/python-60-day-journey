import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_won = 0
computer_won = 0
wants_to_continue = True
game_image = [rock,paper,scissors]
image_name = ["Rock","Paper","Scissors"]\

if wants_to_continue == True:

    print(f"COMPUTER SCORE: {computer_won} and PLAYER SCORE: {player_won}")
    player_input = int(input("What would you like to choose. 0 for rock, 1 for paper, or 2 for scissors. "))
    computer_input = random.randint(0,2)

    if player_input < 0 or player_input > 2:
        print("WRONG INPUT")
    else:
        print(f"Your choice: {image_name[player_input]} {game_image[player_input]}")
        print(f"Computer choice: {image_name[computer_input]}  {game_image[computer_input]}")

        if player_input == computer_input:
            print("Draw")
        elif player_input == 0 and computer_input == 1:
            print("You lose")
            computer_won += 1
        elif player_input == 0 and computer_input == 2:
            print("You win")
            player_won += 1
        elif player_input == 1 and computer_input == 0:
            print("You win")
            player_won += 1
        elif player_input == 1 and computer_input == 2:
            print("You lose")
            computer_won += 1
        elif player_input == 2 and computer_input == 0:
            print("You lose")
            computer_won += 1
        elif player_input == 2 and computer_input == 1:
            print("You win")
            player_won += 1

        print(f"COMPUTER SCORE: {computer_won} and PLAYER SCORE: {player_won}")

        continue_or_not = input("Would you like to play again? Y/N ")

        if continue_or_not.lower() == "n":
            wants_to_continue = False

