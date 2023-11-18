MIN_LENGTH = 8
password = input("Enter password")

while len(password) < MIN_LENGTH:
    print("The password length must be at least greater than 8 bits.")
    password = input("Enter password")
print(len(password) * '*')


