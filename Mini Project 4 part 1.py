# Treasure-Seeker
#Introduction
name = input("Before we get started, what's your name?")
print("Are you ready for an adventure", name, "?")
print("Let's jump right in then, shall we?")

answer = input("Where do you thnk we should start? The old bookstore, the deserted pool, or the abandoned farm?")

if answer == "the deserted pool" or "deserted pool" or "Pool" or "The deserted pool" or "pool" or "the pool" or "Deserted pool" or "deserted pool" or "the pool":
    print("Oooh, a spooky pool? Sure, why not? Lets see if there's even any water left...maybe a drowned spirit?!")
if answer == "the old bookstore" or "the bookstore" or "bookstore" or "The old bookstore" or "Bookstore":
    print("The bookstore huh? Sounds like the lesser of three evils.")
if answer == "the abandoned farm" or "the farm" or "The farm" or "Farm" or "The abandoned farm" or "farm":
    print("Hmm...sounds dangerous..but since you picked it...I guess I must join you. Whatever happens....happens.")

name2 = input("Honestly...there seems to be more to this than meets the eye. Do you trust me ?")
if name2 == "Yes" or name2 =="yes":
    print("Thanks for the confidence boost!")
    answer2 = input("We should move forward...right? *Answer in yes/no")
if answer2 == "Yes" or answer2 == "yes":
    print("Okay...)

if answer2 == "No" or answer2 == "no":
    print("Whew, bye bye.")
    exit(3)

if name == "No" or name == "no":
    print("Ouch, okay. Good luck getting through this without any hints...in fact I suggest you restart the game...cuz you ain’t going nowhere no more.")
    exit()
