import random

computerRole = None
userRole = None
tupleOfStr = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))


# function that accepts list of strings as argument and prints the board
def printGameBoard(gameboard):
    print ("-------------")
    for i in range(3):
        print( "|", gameboard[0+i*3], "|", gameboard[1+i*3], "|", gameboard[2+i*3], "|")
    print("-------------")


# function that checks if the game is over
def checkIfGameFinished():
    for each in win_coord:
        if gameboard[each[0]] == gameboard[each[1]] == gameboard[each[2]]:
            if gameboard[each[0]] == userRole:
                print('You won')
            else:
                print('You lost')
            return True

    counter = 0
    for i in gameboard:
        for y in str(range(10)):
            if (i != y):
                counter +=1
    if(counter) == 9:
        return True
    return False

# function that simulates computer actions
def computerMove():
    statusOfBoard = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    counter = 0
    for each in win_coord:
        for i in each:
            if gameboard[i] == userRole:
                statusOfBoard[counter][0] +=1
            elif gameboard[i] == computerRole:
                statusOfBoard[counter][1] +=1
            elif gameboard[i] not in 'x0':
                statusOfBoard[counter][2] = i
        counter +=1

    for i in statusOfBoard:
        if i[1] == 1 and i[2] != -1:
            gameboard[i[2]] = computerRole
            return 0

    for i in statusOfBoard:
        if i[0] == 1 and i[2] != -1:
            gameboard[i[2]] = computerRole
            return 0

    for i in statusOfBoard:
        if i[1] == 0 and i[2] != -1:
            gameboard[i[2]] = computerRole
            return 0

    listOfEmptyCells = list()
    for i in range(len(gameboard)):
        if (gameboard[i] in tupleOfStr):
            listOfEmptyCells.append(i)
    index = random.choice(listOfEmptyCells)
    gameboard[index] = computerRole


# function that checks if chosen user input for the role ('x' or '0' is valid)
def userMove():
    isInputValid = False
    while not isInputValid:
        userInput = input('Please enter number in the range from 1 to 9: \n')
        if (userInput not in tupleOfStr):
            print('Sorry but the input has to be in the range of 1-9. Please try one more time: ')
            continue
        else:
            if (gameboard[int(userInput) - 1]) in 'x0':
                print('This cell is already taken. Please try one more time')
                continue
            else:
                gameboard[int(userInput) - 1] = userRole
                isInputValid = True

# game running
gameboard = ['1', '2','3','4','5','6','7','8','9']


while True:
    userRole = input('Please choose \'x\' or \'0\': \n')
    if userRole not in 'x0':
        print('Sorry, you must choose between \'x\' or \'0\' ')
        continue
    else:
        break

if(userRole == 'x'):
    computerRole = '0'
else:
    computerRole = 'x'

printGameBoard(gameboard)

while True:

    userMove()

    printGameBoard(gameboard)
    print('-------------------------------------------')

    if checkIfGameFinished():
        break

    computerMove()
    print('Computer has made the move')
    printGameBoard(gameboard)

    if checkIfGameFinished():
        break
