import random


randvar = random.randrange(0,100)
print "Random number has been generated:"
guesed = False

while guessed == False:
    userinp = int(input("your guess please:"))
    if userinp == randvar:
        guesed = True
        print "well done"
    elif userinp > 100:
        print "our guess range is between 0 and 100, please try again:"
    elif userinp < 0:
        print("Our guess range is between 0 and 100, please try a bit higher")
    elif userinp > randvar:
        print("Try one more time, a bit lower")
    elif userinp < randvar:
        print("Try one more time, a bit higher")

    print("End of program")