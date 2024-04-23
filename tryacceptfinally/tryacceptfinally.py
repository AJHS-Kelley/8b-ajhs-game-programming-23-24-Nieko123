# This
# Try -- except -- else -- finally

try: # the code in this block is always executed
    myVariable = 1
    print(myVariable)
    myString = "Five"
    print(float(myString))
except NameError:
    print("There is an incorrect variable name in your code.")
except:
    print("Something else went wrong.")
else:
    print("Code executed correctly with no exceptions.\n")
finally:
    print("I'll be back.\n")



