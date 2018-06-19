# Treasure-Seeker
points = 0
name = input("What's your name?")
print("Hello, I hope your day has being going well so far", name, ".")
points += 2
print("You just earned 2 points! Your total number of points is" , points, "!")
option1 = input("Would you like to go on an adventure?")

if option1 == "Yes" or "yes":
    print ("Lets go!")
    points += 2
    print("You just earned 2 points! Your total number of points is" , points, "!")
elif option1 == "No" or "no":
    print ("Then why are you here", name, "?", "Please direct yourself to the nearest exit." )
    exit()

option2 = input("Should we go to the Arctic or Outer Space? ")
print("Good choice!")
points += 2
print("You just earned 2 points! Your total number of points is" , points, "!")

if (option2 == "The Arctic" or option2 == "the arctic" or option2 == "Arctic" or option2 == "the Arctic"):
    print("Off to The Arctic we go!")
    points += 2
    print("You just earned 2 points! Your total number of points is" , points, "!")
if (option2 == "Outer Space" or option2 == "Outer space" or option2 == "outer Space" or option2 == "outer space"):
    print("To Outer Space!")
    points += 2
    print("You just earned 2 points! Your total number of points is" , points, "!")

option3 = input("Are you ready to have fun!")
if option3 == "Yes" or "yes":
    print ("yeah man!")
    points += 2
    print("You just earned 2 points! Your total number of points is" , points, "!")
    option4 = input("Want an Arctic funfact?")
if option3 == "Yes" or "yes":
    print("Great! Did you know that the name ‘Arctic’ comes from a Greek word meaning ‘near the bear’.")
    option5 = input("Did you think that was a cool fun fact?")
    if option5.lower() == "cool":
        print("( ͡° ͜ʖ ͡°)")
        print("You just earned 2 points! Your total number of points is" , points, "!")
elif option3 == "No" or option3 == "no":
    print ("That's fine my dude, there's always next time", name, "?", "Please direct yourself to the nearest exit." )
    exit()

if option3 == "No" or option3 == "no":
    print("Bye :)")
    print("See you maybe?")
    exit()
