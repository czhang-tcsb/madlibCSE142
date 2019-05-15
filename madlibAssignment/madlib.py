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
i = input()


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
        viewOperation()
    if(CVQ == "q"):
        print("quit activated")
def getFileName():
    GFN = input("Input file name ")
    print("GFN: " + GFN)
    print("this will show us if file exists")
    print(os.path.exists(GFN))
    while(os.path.exists(GFN) == False):
        GFN = input("File not found. Try again: ")
def createOperation():
    print("This is the create operation")
def viewOperation():
    print("This is the view operation")
    getFileName()
    readFile()

def readFile():
    if(i == "clothes.txt"):
        fileToRead = "clothes.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    elif(i == "dance.txt"):
        fileToRead = "dance.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    elif(i == "simple.txt"):
        fileToRead = "simple.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    elif(i == "tarzan.txt"):
        fileToRead = "tarzan.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    else:
        fileToRead = "university.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
readFile()
CVQinput()
#createOperation()
viewOperation()
getFileName()
#CVQinput()
