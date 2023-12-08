# Example Game Function project, Nieko Garnes v0.0
import random

def startRace():
    userChoices = ['yes']
    print("Are you ready to start the race?(yes or no):\n")
    if userChoices:
        userChoices = input().upper()
        userChoices = 'yes' or 'y'
    else:
        print("Get out my face")

startRace()

def hurdleSuccess():
    choices = ['x', 'a', 'w']
    computerChoice = random.choice(choices)

    userChoice = input("enter one of the folowing(X,A,W);\n").lower()

    if userChoice not in choices:
        print("Choice one of the choiceses silly")
        hurdleSuccess()

    print("CPU choice:", computerChoice)
    print("You chose:", userChoice)

    if userChoice == computerChoice:
        print("you and the computer both got over the hurdle!")
    elif (userChoice == 'x' and computerChoice == 'w') or \
         (userChoice == 'a' and computerChoice == 'x') or \
         (userChoice == 'w' and computerChoice == 'a'):
        print("you got over the hurdle and the computer didn't lol!")
    else:
        print("You fell and the computer didn't, loser")
    
hurdleSuccess()

def playAgain():
    userChoices = ['yes']
    print("Do you want to play again? Yes or No?:\n")
    if userChoices:
        userChoices = 'yes' or 'y'
        return input().lower().startswith('y')
    else:
        print("good game")

playAgain()





