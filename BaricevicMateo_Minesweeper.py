import random

def generateMine(n):
    if (random.randint(1, 100) <= n):
        return 1
    else:
        return 0

boardSize = 10
board = [[0 for x in range(0, boardSize)] for y in range(0, boardSize)]
mines = [[generateMine(20) for x in range(0, boardSize)] for y in range(0, boardSize)]
revealed = [[0 for x in range(0, boardSize)] for y in range(0, boardSize)]

def printBoard():
    print("\n   ", end="")
    for x in range(0, boardSize):
        print("%2d" % (x+1), end=" ")
    print()
    for x in range(0, boardSize):
        print(" " + chr(65+x), end=" ")
        for y in range(0, boardSize):
            if revealed[y][x]:
                if board[y][x] == -1:
                    print(" X ", end="")
                else:
                    print(" " + str(board[y][x]) + " ", end="")
            else:
                print("__ ", end="")
        print("\n", end="")

def printMines():
    print("   ", end="")
    for x in range(0, boardSize):
        print("%2d" % (x+1), end=" ")
    print()
    for x in range(0, boardSize):
        print(" " + chr(65+x), end=" ")
        for y in range(0, boardSize):
            print(" " + str(mines[y][x]) + " ", end="")
        print("\n", end="")
        
def generateBoard():
    for x in range(0, boardSize):
        for y in range(0, boardSize):
            if mines[y][x]:
                board[y][x] -= 1
            else:
                if y > 0:
                    if x > 0 and mines[y-1][x-1]:     		# gore-lijevo
                        board[y][x] += 1
                    if mines[y-1][x]:                 		# gore
                        board[y][x] += 1
                    if x < boardSize-1 and mines[y-1][x+1]: # gore-desno
                        board[y][x] += 1
                if x > 0 and mines[y][x-1]:           		# lijevo
                    board[y][x] += 1
                if x < boardSize-1 and mines[y][x+1]:       # desno
                    board[y][x] += 1
                if y < boardSize-1:
                    if x > 0 and mines[y+1][x-1]:     		# dolje-lijevo
                        board[y][x] += 1
                    if mines[y+1][x]:                 		# dolje
                        board[y][x] += 1    
                    if x < boardSize-1 and mines[y+1][x+1]: # dolje-desno
                        board[y][x] += 1

def revealZeros(x, y):
    if x < 0 or x > boardSize-1 or y < 0 or y > boardSize-1:
        return
    if board[y][x] > 0 and not revealed[y][x]:
        revealed[y][x] = 1
    if board[y][x] == 0 and not revealed[y][x]:
        revealed[y][x] = 1
        revealZeros(x-1, y-1)  # gore-lijevo
        revealZeros(x-1, y)    # gore
        revealZeros(x-1, y+1)  # gore-desno
        revealZeros(x, y-1)    # lijevo
        revealZeros(x, y+1)    # desno
        revealZeros(x+1, y-1)  # dolje-lijevo
        revealZeros(x+1, y)    # dolje
        revealZeros(x+1, y+1)  # dolje-desno
    else:
        return

def won():
    if sum(map(sum, revealed)) == boardSize*boardSize - sum(map(sum, mines)):
        return 1
    return 0

def game():
    #printMines()
    print("Minesweeper")
    generateBoard()
    printBoard()
    while True:
        unos = input("\nInput coords (XY): ")
        if unos == "q":
            break
        if len(unos) < 2 or len(unos) > 3 or ord(unos[0])-65 < 0 or ord(unos[0])-65 > boardSize-1 or int(unos[1:3]) < 1 or int(unos[1:3]) > boardSize:
            print("Wrong input!")
            continue
        if board[int(unos[1:3])-1][ord(unos[0])-65] == 0:
            revealZeros(ord(unos[0])-65, int(unos[1:3])-1)
        revealed[int(unos[1:3])-1][ord(unos[0])-65] = 1
        printBoard()
        if board[int(unos[1:3])-1][ord(unos[0])-65] == -1:
            print("\nBooooom! You lost :/")
            break
        if won():
            print("\nCongratulations! You won! :D")
            break

game()
input("\nPress enter to exit...")