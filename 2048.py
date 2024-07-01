import random
#starting board
def startBoard(gridWidth):
    startingGrid = []
    for i in range(gridWidth): 
        startingList = []
        for i in range(gridWidth):
            startingList.append(0)
        startingGrid.append(startingList)
    return startingGrid
def printBoard(board, gridWidth):
    for i in range(gridWidth):
        print(board[i])
#randomizer that returns list value [row,column]
def randomizer(board, gridWidth):
    while True:
        rowNumb = random.randint(0,gridWidth-1) 
        columnNumb = random.randint(0,gridWidth-1)
        if board[rowNumb][columnNumb] == 0:
            return [rowNumb, columnNumb]
def addTwo(board):
    twoXY = randomizer(board, len(board))
    x = random.randint(1,2)
    if x == 1:
        x = 2
    elif x == 2:
        x = 4
    board[twoXY[0]][twoXY[1]] = x
    return board
def shiftRight(list):
    #Combine values from right to left
    for i in range(len(list)-1, 0, -1): #counts length-1 and down. needs to check for combine
        x1 = 1
        if list[i] != 0:
            while True: #combines the values
                if i - x1 >= 0:
                    if list[i-x1] == 0:
                        x1 += 1
                    else: 
                        if list[i] == list[i-x1]: #evaluates if last index and 2nd to last is equal
                            list[i] *= 2 #if so, last index is double.
                            list[i-x1] = 0
                            break
                        else:
                            break
                else:
                    break
    #shifts values to the right
    for y in range(len(list)-1,0,-1):
        x2 = 1
        while y-x2 >= 0: #cant go out of range with this.
            if list[y] == 0: 
                if list[y-x2] > 0:
                    list[y] = list[y-x2]
                    list[y-x2] = 0
                    break
                else:
                    x2 += 1
            else:
                break
    return list   
def rightFunction(board):
    for i in range (len(board)):
        board[i] = shiftRight(board[i])
    return board
def shiftLeft(list):
    for i in range(len(list)-1): #counts 0 to length of list - 1
        x1 = 1
        if list[i] != 0: #as long as that value isn't 0, it can be combined
            while True: #combines the values
                if i + x1 < len(list):
                    if list[i+x1] == 0:
                        x1 += 1
                    else: 
                            if list[i] == list[i+x1]: #if the number and the nonzero number to the right of the number are equal, add them
                                list[i] *= 2 #i is doubled
                                list[i+x1] = 0
                                break
                            else:
                                break
                else:
                    break
    for y in range(len(list)): #shifting all values left
        x2 = 1
        while y+x2 < len(list): #cant go out of range with this.
            if list[y] == 0: 
                if list[y+x2] > 0:
                    list[y] = list[y+x2] #swap places
                    list[y+x2] = 0
                    break
                else:
                    x2 += 1
            else:
                break #break if the current position has a value
    return list
def leftFunction(board):
    for i in range (len(board)):
        board[i] = shiftLeft(board[i])
    return board
def flipMatrix(board):
    board2 = []
    for _ in range (len(board)):
        tempList = []
        for i in range (len(board)):
            tempList.append(0)
        board2.append(tempList)
    for x in range(len(board)):
        for y in range(len(board)):
            board2[x][y] = board[y][x]
    return board2    
#start of main
print("Hi, Welcome to 2048.")
gridWidth = 4
board = startBoard(gridWidth)
userInput = ""
for i in range(4): 
    board = addTwo(board)
printBoard(board, gridWidth)
while True:
    userInput = input("Which direction?: ")
    if userInput == "d":
        board = rightFunction(board)
    if userInput == "a":
        board = leftFunction(board)
    if userInput == "s":
        board = flipMatrix(rightFunction(flipMatrix(board)))
    if userInput == "w":
        board = flipMatrix(leftFunction(flipMatrix(board)))
    addTwo(board)
    printBoard(board, gridWidth)
