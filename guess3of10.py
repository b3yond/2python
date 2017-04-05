#! /usr/bin/env python
from random import randint

print "Guess a number between 1 and 10. You have 3 tries."
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    else:
        guesses_left -= 1
        if guesses_left > 0:
            print "Try again!"
        elif guesses_left == 0:
            print "You lose."
            print "The Number was " + str(random_number) + "."
            break
else:
    print "You win."
