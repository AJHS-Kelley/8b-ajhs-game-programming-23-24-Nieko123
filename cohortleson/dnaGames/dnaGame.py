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

dna = genDNA()
rna = doTranscription(dna)
print(verifySequence(dna, rna[0]))

