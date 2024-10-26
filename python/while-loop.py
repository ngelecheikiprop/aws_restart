#!/usr/bin/python3

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGeussRight = False

while isGeussRight != True:
    geuss = input("Geuss number between 1 and 10: ")
    if int(geuss) == number:
        print("you made the right geuss")
        isGeussRight = True
    else:
        print("You geussed {}. sorry, that is not the right answer".format(geuss))
        