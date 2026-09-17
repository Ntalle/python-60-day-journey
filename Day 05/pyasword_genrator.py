import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random_letters = []
random_symbols = []
random_numbers = []
password = ""

num_of_letters = int(input("How many letters would you like to generate? Between 1 to 52. "))

num_of_numbers = int(input("How mane numbers would you like to generate? Between 1 to 10. "))

num_of_symbols = int(input("How many symbols would you like to generate? Between 1 to 9. "))

for l in range(num_of_letters):
    random_letters.append(random.choice(letters))
for n in range(num_of_numbers):
    random_numbers.append(random.choice(numbers))
for s in range(num_of_symbols):
    random_symbols.append(random.choice(symbols))

whole_list = random_letters + random_numbers + random_symbols
random.shuffle(whole_list)

for item in whole_list:
    password += item

print(f"\nYour generated password is: {password}")