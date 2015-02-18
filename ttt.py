#tic tac toe.
import random

player1 = "X"               # value of X for the first player
player2 = "O"               # value of O for the second player
board = []                  # array that holds the characters for the board
win = False                 # win boolean ceck
turn = 0                    # variabe to marks who's turn it is
name1 = ""                  # name of the first player
name2 = ""                  # name of the second player
moves = 0                   # moves made

def display():
    print "\n Welcome to the game of tic-tac-toe \n"


def makeBoard():
    #this function initializes the board with the numbers at first.
    for i in range(1,10):
        board.append(str(i))

def printBoard():
    # this function prints the board
    print"""
     %s | %s | %s
    ------------
     %s | %s | %s
    ------------
     %s | %s | %s """ % (board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1], board[2])

def initializeBoard():
    # initialize the board to black spacces.
    del board[:]
    for i in range (1,10):
        board.append(" ")

def checkIn(position):
    # this will check to see if the input is a valid input
    # returns true or false.

    position = int(position)
    position -= 1

    if position > 8 or position < 0:
        print "Your position selection is not within the range of selection (1-9). Please Choose another."
        return False
    elif board[position] == "X" or board[position] == "O":
        print "This position has already been chosen. Please choose another."
        return False
    else:
        return True

def getInput(player):
    # this funcition will get input and then send it to the checker to make sure that
    # it is a valid input, if it isn't it will keep asking for an input until a proper
    # input is given.

    pos = -1
    check = False

    while check == False:
        pos = raw_input("What is the position that you want to play?\n>")
        check = checkIn(pos)

    setInput(pos,player)


def setInput(position, player):
    # this function will set input into the board.
    position = int(position)
    position -= 1
    board.insert(position,player)
    board.pop(position + 1)

def winCheck(player):
    #function will check for a winner and return true or false.

	# diagonal wins
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False
	
    #horizontal wins
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True

    #vertical wins
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True


turn = random.randint(1,2)		# determin player for first move.
display()			#dispay the welcome message and get player names
name1 = raw_input("Player 1 input your name:\n>")
name2 = raw_input("Player 2 input your name:\n>")
makeBoard()			#make the board list
printBoard()		#display outlay of the board
initializeBoard()	#initialize board

while win == False or moves < 9:
    if turn == 1:
        moves += 1
        print "\n%s's turn" % name1
        getInput(player1)
        printBoard()
        win = winCheck(player1)
        if win == True:
            print "\n %s has won the match! \n" % name1
            break
        turn = 2
    else:
        moves += 1
        print "\n%s's turn" % name2
        getInput(player2)
        printBoard()
        win = winCheck(player2)
        if win == True:
            print "\n %s won the match! \n" % name2
            break
        turn = 1


if moves == 9 and win == False:
    print "\n Game over: tie \n"
