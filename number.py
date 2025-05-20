import random

print 
print ("Welcome to the game! Lets see how good your number guessing skills are")
    
highNumb = int(input("What is the highest value in the range starting from 0? "))
striker = int(input("How many chances do you want to get? "))

print()

x = (random.randrange(0,highNumb))

wrongs = int(0)
status = "in play"

def checker (y):
    global wrongs
    global status
    
    if wrongs == striker:
        print ("Yikes! You've striked out. The number was " + str(x))
        status = "out"
    elif y == x:
        status = "win"
        print ("Yay you won!")
    elif y < x:
        wrongs += 1
        print ("Go higher. Strikes = " + str(wrongs))
    elif y > x:
        wrongs += 1
        print("Go lower. Strikes = " + str(wrongs))
    print ()

while (wrongs < striker) or (status == "in play"):
    guess = int(input ("Guess! "))
    checker (guess)

if wrongs == striker:
    print ("HAHA you lost! The number was " + str(x))
elif status == "win":
    print (" :) ")



