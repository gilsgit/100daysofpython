
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_array = []


for letter in range(1, (nr_letters + 1)):
    letter_length = len(letters)
    letter_amount = random.randint(0, (letter_length - 1))
    print(letters[letter_amount])
    password_array.append(letters[letter_amount])
    print(password_array)

for symbol in range(1, (nr_symbols + 1)):
    symbol_length = len(symbols)
    symbol_amount = random.randint(0, (symbol_length - 1))
    print(symbols[symbol_amount])
    password_array.append(symbols[symbol_amount])
    print(password_array)

for number in range(1, (nr_numbers + 1)):
    number_length = len(numbers)
    number_amount = random.randint(0, (number_length - 1))
    print(numbers[number_amount])
    password_array.append(numbers[number_amount])
    print(password_array)

#shuffle password list characters
random.shuffle(password_array)
print(password_array)

#add all characters together in one string
password = ""
for char in password_array:
    password += char

print(f"Your password is: {password}")

