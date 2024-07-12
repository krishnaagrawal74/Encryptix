import random
import string

def passwordGenerator():
    len = int(input("Enter the length of the password: "))

    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # creating an array of all lowercase and uppercase letters, digits and symbols
    allCharacters = lowerCase + upperCase + digits + symbols

    # generating a array of length equal to user input consisting of random characters from the above array created
    x = random.sample(allCharacters,len)

    # converting the password array to string and returning the same to user
    password = "".join(x)
    print(password)
    print()

    passwordGenerator()

passwordGenerator()

# note that the symbols used can be restricted by feeding our own array of allowed symbols as per the application demand
