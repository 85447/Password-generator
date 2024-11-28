import random
import string

def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    password_length = int(input("Enter the desired password Lenmgth:"))

    if password_length < 1:
        print("Password length must be at least 1 Charachter")
    else:
        generate_password = generate_password(password_length)
        print("Generated Password:", generate_password)