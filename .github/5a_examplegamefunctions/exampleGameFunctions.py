# Example Game Function project, Nieko Garnes v0.0
import random

def startRace():

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
    
    playAgain = input("Want to run it back? (yes/no):\n").lower()
    if playAgain == 'yes':
        playAgain()
    else:
        print("it's been fun bye")

def raceOutcome(param1, param2, param3):
    pass

def raceOutcome(laps, speed, place):
    if laps > 1 and speed >= 50 and place == 'Won':
        raceOutcome = True
    elif laps > 1 and speed >= 50 and place == 'lose':
        raceOutcome = False
    else:
        print(' Aww man, You lose!\n')
        raceLose = True
        return raceLose
    return raceOutcome


#i like to chase 1 year olds because they're fun to tickle