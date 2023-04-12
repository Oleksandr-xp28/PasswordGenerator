try:
    import random
    import string

    numbers = string.digits
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    special_chars = string.punctuation

    char_pool = ''

    while True:
        password_length = int(input("Enter the password length: "))
        if password_length <= 0:
            print("Password length must be greater than 0")
        elif password_length > 100:
            print("Password length must be less than or equal to 100")
        else:
            break

    while True:
        use_special_chars = input("Do you want to use special characters? (y/n): ")
        if use_special_chars.lower() == 'y':
            char_pool += special_chars
            break
        elif use_special_chars.lower() == 'n':
            pass
            break
        else:
            print("Please enter y or n")

    while True:
        use_numbers = input("Do you want to use numbers? (y/n): ")
        if use_numbers.lower() == 'y':
            char_pool += numbers
            break
        elif use_numbers.lower() == 'n':
            pass
            break
        else:
            print("Please enter y or n")

    while True:
        use_uppercase = input("Do you want to use uppercase letters? (y/n): ")
        if use_uppercase.lower() == 'y':
            char_pool += uppercase_letters
            break
        elif use_uppercase.lower() == 'n':
            pass
            break
        else:
            print("Please enter y or n")

    while True:
        use_lowercase = input("Do you want to use lowercase letters? (y/n): ")
        if use_lowercase.lower() == 'y':
            char_pool += lowercase_letters
            break
        elif use_lowercase.lower() == 'n':
            pass
            break
        else:
            print("Please enter y or n")

    if not char_pool:
        print("Error: No character sets selected")
    else:
        password = ''.join(random.choice(char_pool) for i in range(password_length))
        print("Your generated password is:", password)
except Exception:
    print("Error: Invalid input")