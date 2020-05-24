'''
Moataz Khallaf
chemConveter
Nov 8, 2018
'''
###imports
import sys
import random
### Vars
PEl = 0
NEl = 0
again = 0
#literally no reason to ever ever use a tuple when you can just use an array
tokentuple = ("hi", "kids", "this", "is", "a", "tuple")

nTable = [
    [1, "F", 18.998403, 1, 1], # It's number in list, element, molar mass and negative charge
    [2, "Cl", 35.453, 1, 1],
    [3, "Br", 79.904, 1, 1],
    [4, "i", 126.90447, 1, 1],
    [5, "SO4", 96.06, 2, 1]
]

pTable = [
    [1, "Li", 6.941, 1, 1], # It's number in list, element, molar mass and positive charge and number in balence
    [2, "Mg", 24.305, 2, 1], #The idea behind the last one is that it's added to the El in a function to balence
    [3, "Ca", 40.078, 2, 1], # it
    [4, "Sr", 87.62, 2, 1],
    [5, "Ba", 137.327, 2, 1],
    [6, "Fe", 55.845, 2, 1],
    [7, "Hg2", 200.59, 2, 1],
    [8, "Pb", 207.2, 2, 1],
    [9, "Cu", 63.546, 1, 1],
    [10, "Ag", 107.8682, 1, 1],
    [11, "Ti", 47.867, 1, 1],
    [12, "Ca", 40.078, 2, 1],
    [13, "Ra", 226, 2, 1]
]

###Inputs Funcs
def menu(): #just for funzies I'm adding a menu
    cough =  (input("Yo what's up cool chemistry kids, want to do some calculations? (Y/N)"))
    cough = cough.lower
    if cough == "y" or cough == "yes":
            print("make sure to write the elements right or Mr.Johnson will mess you up")
    else:
            sys.exit()

def askElement1():
    x = input("What is your positive element? (+) ")
    return x

def askVolume():
    x = float(input("What is your volume? (L) "))
    return x

def askConc():
        x = float(input("What is your concentration? (mol/L) "))
        return x

def askElement2():
    x = input("What is your negative element? (-) ")
    return x

###Processing Funcs
def testNum(x):
    try:
        x = float(x)
        return x
    except ValueError:
        x = input("enter a valid number")
        return testNum(x)

def molEq(a,b):
        x = a * b
        return x

def findLimit(a,b):
        if a > b:
                return b
        else:
                return a
        
#def balence(a, b):

###Outputs Funcs

### --- Actual code starts here !!!
x = input("before we start enter 1 for a meme")
if x == "1":
        easterEgg = list()
        with open('egg.txt') as f:
                for line in f:
                        easterEgg.append(line.strip())
        print(easterEgg)
menu()
print(tokentuple)
while True:
        ###Inputs
        while True:
                ##pos in

                PEl = askElement1() ## positive element pick
                posVolume = (askVolume()) ##I feel like the function name is good enough
                testNum(posVolume)
                posConc = (askConc()) ##conc = concentration
                testNum(posConc)
                ##neg in

                NEl = askElement2() ## negative element pick
                negVolume = (askVolume())
                testNum(negVolume)
                negConc = (askConc())
                testNum(negConc)

                ##making sure pre will form...

                if (NEl == "F") and (PEl == "Li" or PEl == "Mg" or PEl == "Ca" or PEl == "Sr" or PEl == "Ba" or PEl == "Fe" or PEl == "Hg" or PEl == "Pb") :
                        break

                elif (NEl == "Cl" or NEl == "Br" or NEl == "I") and (PEl == "Cu" or PEl == "Ag" or PEl == "Hg" or PEl == "Pb" or PEl == "Ti"):
                        break

                elif (NEl == "SO4") and (PEl == "Ca" or PEl == "Sr" or PEl == "Ba" or PEl == "Ag" or PEl == "Hg" or PEl == "Pb" or PEl == "Ra"):
                        break
                else:
                        print("you picked the wrong elements mate, that means it won't percipitate")
        ###Processing


        for i in range(len(pTable)): ##checks if positive element is in list
                if PEl == pTable[i][1]:
                        PEl = pTable[i]
                        for i in range(len(nTable)): ##checks if negative element is in list
                                if NEl == nTable[i][1]:
                                        NEl = nTable[i]

        if NEl[3] > PEl[3]: ## balence charge for -2,+1
                PEl[3] = PEl[3] + 1
                PEl[4] = PEl[4] + 1
        elif NEl[3] < PEl[3]: ## balence charge for -1,+2
                NEl[3] = NEl[3] + 1
                NEl[4] = NEl[4] + 1
        else:
                pass

        ##LR mols
        posMol = molEq(posVolume, posConc) / PEl[4]
        negMol = molEq(negVolume, negConc) / NEl[4]

        mol = findLimit(posMol, negMol)
        mass = ((PEl[2] * PEl[4]) + (NEl[2] * NEl[4]))
        massP = mass * mol


        ###Outputs

        print("your balenced equation is ", PEl[1], PEl[4], NEl[1],  NEl[4])

        if mol == negMol:
                print("LR is ",NEl, negMol," mol")
        else:
                print("LR is",PEl, posMol," mol")

        print(massP)

        again = input("Y for again")
        again.lower
        if again == "y":
                pass
        else:
                break
                sys.exit()