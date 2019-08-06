import os
import random

computerRole = None
userRole = None
numUserInput = None
tupleOfStr = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

# function that accepts list of strings as argument and prints the board
def printGameBoard(gameboard):
    print ("-------------")
    for i in range(3):
        print( "|", gameboard[0+i*3], "|", gameboard[1+i*3], "|", gameboard[2+i*3], "|")
    print("-------------")


# function that checks if the game is over
def checkIfGameFinished():
    isFinished = False
    winner = 0
    if (gameboard[0] == gameboard[3] == gameboard[6]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[1] == gameboard[4] == gameboard[7]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[2] == gameboard[5] == gameboard[8]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[0] == gameboard[1] == gameboard[2]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[3] == gameboard[4] == gameboard[5]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[6] == gameboard[7] == gameboard[8]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[0] == gameboard[4] == gameboard[8]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')

    elif (gameboard[2] == gameboard[4] == gameboard[6]):
        isFinished = True
        if gameboard[0] == userRole:
            print('You won')
        else:
            print('You lost')
    else:
        counter = 0
        for i in gameboard:
            if (i not in '123456789'):
                counter +=1
        if(counter) == 9:
            print('It is a draw')
            isFinished = True
        return isFinished

    return isFinished

# function that checks if chosen user input for the role ('x' or '0' is valid)
def checkIfChosenSymbolIsValid(userInput):
    isInputValid = False
    tupleOfValidUserInputs = ('x', '0')
    for i in tupleOfValidUserInputs:
        if userInput == i:
            isInputValid = True
            break
    return isInputValid


# function that checks if user input to complete the move is in the range of 1-9
def checkIfNumInputValid(userInput):
    isInputValid = False
    for i in tupleOfStr:
        if userInput == i:
            isInputValid = True
            break
    return isInputValid

# function that makes the move from computer side (first it looks for rows that have 2 cells filled with same input ('0' or 'x') and in case of their absence random cell is taken from all free)
def computerMove():
    print('Now it is turn for computer to make the move \n')
    while True:
        isMoveDone = False
        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(3):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '123'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(3,6):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '456'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(6,9):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '789'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        for i in range(0,7,3):
            index = -1
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '147'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(1,8,3):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '258'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(2,9,3):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '369'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(0,9,4):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '159'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        userMovescounter  = 0
        computerMovescounter  = 0
        index = -1
        for i in range(2,7,2):
            if (gameboard[i] == userRole):
                userMovescounter +=1
            if (gameboard[i] == computerRole):
                computerMovescounter +=1
            if (gameboard[i] in '357'):
                index = i
        if (userMovescounter == 2 or computerMovescounter == 2) and index != -1:
            gameboard[index] = computerRole
            isMoveDone = True
        if (isMoveDone):
            break

        listOfEmptyCells = list()
        for i in range(len(gameboard)):
            if (gameboard[i] in '123456789'):
                listOfEmptyCells.append(i)
        index = random.choice(listOfEmptyCells)
        gameboard[index] = computerRole
        print('Computer has made the move')
        break

# function that accepts user input (1-9) and in case chosen cell is empty it assigns new value to it
def userMove(userInput):
    if userInput == '1' and gameboard[0] == '1':
        gameboard[0] = userRole
    elif userInput == '2' and gameboard[1] == '2':
        gameboard[1] = userRole
    elif userInput == '3' and gameboard[2] == '3':
        gameboard[2] = userRole
    elif userInput == '4' and gameboard[3] == '4':
        gameboard[3] = userRole
    elif userInput == '5' and gameboard[4] == '5':
        gameboard[4] = userRole
    elif userInput == '6' and gameboard[5] == '6':
        gameboard[5] = userRole
    elif userInput == '7' and gameboard[6] == '7':
        gameboard[6] = userRole
    elif userInput == '8' and gameboard[7] == '8':
        gameboard[7] = userRole
    elif userInput == '9' and gameboard[8] == '9':
        gameboard[8] = userRole
    elif userInput == '10' and gameboard[9] == '10':
        gameboard[9] = userRole


gameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

tempRoleInput = input('Please choose \'x\' or \'0\': \n')

while not(checkIfChosenSymbolIsValid(tempRoleInput)):
    print('Sorry, you must choose between \'x\' or \'0\' ')
    tempRoleInput = input('Please choose \'x\' or \'0\': \n')

userRole = tempRoleInput

if(userRole == 'x'):
    computerRole = '0'
else:
    computerRole = 'x'

printGameBoard(gameboard)

while True:

    tempNumInput = input('Please enter numeric number in the range 1-9 to make a move: \n')

    while not(checkIfNumInputValid(tempNumInput)):
        print('Sorry, you must enter numeric number from the range 1-9')
        tempNumInput = input('Please enter numeric number in the range 1-9 to make a move: \n')

    while True:
        if gameboard[int(tempNumInput) -1] in 'x0':
            print('You are trying to overwrite the cell')
            tempNumInput = input('Please enter numeric number in the range 1-9 to make a move: \n')
        else:
            numUserInput = tempNumInput
            break


    userMove(numUserInput)
    printGameBoard(gameboard)

    if checkIfGameFinished():
        break

    computerMove()
    printGameBoard(gameboard)

    if checkIfGameFinished():
        break
