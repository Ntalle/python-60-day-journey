print("Welcome to our ticktet counter!!")
user_input = input("Please enter your height in cm. ")
bill = 0
if user_input.isdigit():
    height = int(user_input)

    if height >= 120:
        user_input_age = input("What is your age? ")

        if user_input_age.isdigit():
            age = int(user_input_age)

            if age < 12:
                print("You need to pay $8")
                bill = 8
            elif age < 18:
                print("You need to pay $10")
                bill = 10
            elif age >= 18:
                print("You need to pay $15")
                bill = 15

            wants_photo = input("Would you like to see a photo of you? (y/n) ")

            if wants_photo.lower() == "y":
                bill += 2
            elif wants_photo.lower() == "n":
                bill += 0
            else:
                print("Wrong input")
        else:
            print("Wrong input")

    else:
        print("You are not eligible for this ride. Sorry.")

    print(f"Your final bill is: ${bill}")
else:
    print("Wrong input")

