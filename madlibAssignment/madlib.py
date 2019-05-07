import os
'''
print(os.path.isfile('./test.txt'))
print("This is madlib.py and i hate tacos ")
'''
#intro message
print("Welcome to the game of Mad Libs.")
print("I will ask you to provide various words")
print("and phrases to fill in a story.")
print("The result will be written to an output file.")



def CVQinput():
    CVQ = input("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ")
    print("This is CVQ: " + CVQ)
    CVQ = CVQ.lower()
    print("This is CVQ after lowercased: " + CVQ)
    while (CVQ != "c" and CVQ != "v" and CVQ != "q"):
        CVQ = input("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ")
        print("This is CVQ: " + CVQ)
    if(CVQ == "c"):
        print("create function activated")
        getFileName()
    if(CVQ == "v"):
        print("view function activated")
    if(CVQ == "q"):
        print("quit activated")
def getFileName():
    GFN = input("Input file name ")
    print("GFN: " + GFN)
    print("this will show us if file exists")
    print(os.path.exists(GFN))
    while(os.path.exists(GFN) == False):
        GFN = input("Input File name ")    
def createOperation():
    print("This is the create operation")
def viewOperation():
    print("This is the view operation")

#CVQinput()
#createOperation()
#viewOperation()
getFileName()
