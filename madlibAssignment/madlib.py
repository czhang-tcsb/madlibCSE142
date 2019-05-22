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
GFN = ""
#madlibBool = 1


def CVQinput():
    madlibBool = 1
    while(madlibBool == 1):
        CVQ = input("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ")
        #print("This is CVQ: " + CVQ)
        CVQ = CVQ.lower()
        #print("This is CVQ after lowercased: " + CVQ)
        while (CVQ != "c" and CVQ != "v" and CVQ != "q"):
            CVQ = input("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ")
        #    print("This is CVQ: " + CVQ)

        if(CVQ == "c"):
            print("create function activated")
            #getFileName()
        if(CVQ == "v"):
            print("view function activated")
            viewOperation()
        if(CVQ == "q"):
            print("quit activated")
            madlibBool = 0

def getFileName():
    global GFN
    print("GFN before assingment: " + GFN)
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
    global GFN
    print("This is GFN " + str(GFN))
    fileToRead = GFN
    fileReader = open(fileToRead)
    lines = fileReader.readlines()
    print(lines)
    for x in range(0, len(lines)):
        print(lines[x])
    fileReader.close()
    '''
    if(input == "clothes.txt"):
        GFN = 1
    if(GFN == 1):
        fileToRead = "clothes.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    if(input == "dances.txt"):
        GFN = 2
    elif(GFN == 2):
        fileToRead = "dance.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    if(input == "simple.txt"):
        GFN = 3
    elif(GFN == 3):
        fileToRead = "simple.txt"
        fileReader = open(fileToRead)
        lines = fileReader.readlines()
        print(lines)
        for x in range(0, len(lines)):
            print(lines[x])
        fileReader.close()
    if(input == "tarzan.txt"):
        GFN = 4
    elif(GFN == 4):
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
    '''
#readFile()
CVQinput()
#createOperation()
#viewOperation()
#getFileName()
