# DNA Replicated, Nieko Garnes v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the Specific tool.
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# Game Fuctions
def gameIntro() -> None:
    pass

def genDNA() -> str:
    bassesGenerated = 0
    bassesRequested =int( input("Please Enter a positive interger number of bases to generate.\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        dnaGenerated ==1
    return dnaSequence

dna = genDNA()

def doTranscription(dnaSequence: str) -> tuple:
    print(f"The DNA sequenceis {dnaSequence}.\n")
    print("Youwill now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 jan. 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return(rnaSequence, rnaTime)
    # tuples are ordered -- you can reference elements with the index.
    # tuples are UNCHANGEABLE -- you cannot add, modify, or delte after creating
    # tuples can have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are different lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase "C" and rnaBase == "C"
            isMatch = True
        elif dnaBase "G" and rnaase == "C"
            isMatch = True
        elif dnaBase "T" and rnaBase =="A"
            isMatch = True
        else:
            print ("Unable to identify correct base so no match.\n")
    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 1.0:
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 15.0:
        score += 700000
    else: # slowest time
        score += 250000

    scoreMulti = 0.0
    if len(rnaSequence) > 30:
    scoreMulti = 5.0
    elif
    elif len(rnaSequence) >= 5:
        scoreMulti = 1.0
    else:
        scoreMulti = 0.5
    score *= scoreMulti 
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your first name?\n")
    fullName = playerName + " " + ".txt"
    fileName = "dnaRep"
    saveData = open(fileName, a)

    # File Modes
    #"x mode -- Create File, if file exists, exit with error"
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- Create FILE, FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveDta.write(f"Score: {score}\n")
    saveData.write(f"{datetime.datetime.now()}\n")    

dna = genDNA()
rna = doTranscription(dna)
print(verifySequence(dna, rna[0]))

print(calcScore(rna[0], rna[1]))

