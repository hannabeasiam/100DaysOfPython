import sys


"""
    Never use password check like this, this is only for while loop example
"""

# constant value placed on on top of the file
MASTER_PASSWORD = 'testpassword'
password = input("Please enter the password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town")