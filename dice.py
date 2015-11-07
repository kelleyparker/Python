import random

def roll():
    decision = input("Do you want to roll 1 die, or 2 dice?")
    if decision == 1:
        print random.randint(1,6)
    elif decision == 2:
        print random.randint(1,6)
        print random.randint(1,6)
    else:
        print("Wrong answer! Program ends now!!")


roll()
tryAgain = input("Do you want to roll more dice? 1 for yes, else type anything")

if tryAgain==1:
    roll()
else:
    print("Program Ends NOW!")
