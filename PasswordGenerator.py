import random
import string

numbers = string.digits
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
special_chars = string.punctuation

char_pool = ''

while True:
    try:
        password_length = int(input("Enter the length of password: "))
        if password_length < 1:
            print("Password length must be greater than 1")
            continue
        elif password_length > 20:
            print("Password length must be less than 20")
            continue
        else:
            break
    except ValueError:
        print("Password length must be an integer")
        continue

while True:
    number = input("Use numbers in password? (y/n)" )
    if number.lower() == "y":
        char_pool += numbers
        break
    elif number.lower() == "n":
        break
    else:
        print("Please enter y or n")
        continue

while True:
    symbol = input("Use symbols in password? (y/n)" )
    if symbol.lower() == "y":
        char_pool += special_chars
        break
    elif symbol.lower() == "n":
        break
    else:
        print("Please enter y or n")
        continue

while True:
    upper = input("Use uppercase letters in password? (y/n)" )
    if upper.lower() == "y":
        char_pool += uppercase_letters
        break
    elif upper.lower() == "n":
        break
    else:
        print("Please enter y or n")
        continue

while True:
    lower = input("Use lowercase letters in password? (y/n)" )
    if lower.lower() == "y":
        char_pool += lowercase_letters
        break
    elif lower.lower() == "n":
        break
    else:
        print("Please enter y or n")
        continue

if not char_pool:
    print("Error: No character sets selected")
else:
    password = ''.join(random.choice(char_pool) for i in range(password_length))
    print("Your generated password is:", password)
