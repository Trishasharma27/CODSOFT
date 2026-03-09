import random
import string
length = int(input("Enter the password length: "))
num_passwords = int(input("How many passwords do you want to generate? "))
if length <= 0:
    print("Password length must be greater than 0")
    exit()
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_characters = letters + digits + symbols
for i in range(num_passwords):
    password_list = []
    for j in range(length):
        char = random.choice(all_characters)
        password_list.append(char)
    password = "".join(password_list)
    print("Password", i+1, ":", password)
    if length < 6:
        print("Strength: Weak")
    elif length <= 10:
        print("Strength: Medium")
    else:
        print("Strength: Strong")
    print()
