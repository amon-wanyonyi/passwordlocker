# Password Manager
import random
import string

# import username as username
import username


def store_password():
    # Usernames
    username: str = str(input("Your username: "))


# Website
website = str(input("Enter Website: "))

# Generate Random Password
digit = int(input("How any digits do you want? (integer only)"))
password = ""
for i in range(digit):
    char = random.choice(string.ascii_letters)
    password += char

# Store the password into a file
f = open("password.txt", "a")
f.write(f"{username}-{website}-{str(password)}\n")
f.close()

print(f"Here's your password: {password}")


def search():
    username_or_website = str(input("Do you want to search for username or website? "))
    value = str(input("What value? "))
    f = open("password.txt", "r")
    for line in f:
        info = line.split("-")
        if username_or_website == "username":
            if value == info[0]:
                return info[2]
            # search by username
        else:
            # search by website
            if value == info[1]:
                return info[2]
