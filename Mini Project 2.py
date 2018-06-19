# TreasureSeeker
from random import *
aRandomNumber = randint(1, 20)
guess = 0
guesscounter = 0
while guess != aRandomNumber and guesscounter<4:
    guess = int(input("Guess a number between 1 and 20:"))
    guesscounter +=1
    if guess == aRandomNumber:
        print("You got it right!:)")
        break

    if (guess<aRandomNumber):
        print("The number you entered is too low, guess higher!")
    if (guess>aRandomNumber):
        print("The number you entered is too high, guess lower!")

if guesscounter>3:
    print("You have run out of guesses :(")
