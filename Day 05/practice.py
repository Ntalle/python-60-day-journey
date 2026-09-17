import random
print("Welcome to the number guessing game.\nI will think about a number from 1 to 100.\nI have thought about an number now.\n")

random_number = random.randint(1, 100)
num_of_guesses = 5
guessed_number = 0

guessed_number = int(input("Try to guess my number: "))

for i in range(num_of_guesses):

    if guessed_number == random_number:
        print("You guessed my number! Congratulations!")
        break
    else:
        if guessed_number > random_number:
            print("You guessed too high!")
            num_of_guesses -= 1
            print(f"You have {num_of_guesses} guesses left")
            guessed_number = int(input("Try again: "))
        elif guessed_number < random_number:
            print("You guessed too low!")
            num_of_guesses -= 1
            print(f"You have {num_of_guesses} guesses left")
            guessed_number = int(input("Try again: "))
        elif guessed_number < 1 or guessed_number > 100:
            print("Your guessed number is out of range!")
            num_of_guesses -= 1
            print(f"You have {num_of_guesses} guesses left")
            guessed_number = int(input("Try again: "))

print(f"\nYou lost! My guessed number is {random_number}")
