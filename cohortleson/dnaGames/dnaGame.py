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
print(dna)
