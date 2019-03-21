# deszczyk

from random import randint
from time import sleep

def clear():
	print(chr(27) + "[2J")
    #print("\033[2J")

board=[]
def board_fill(board):
    for i in range(0, 40):
        board.append([" "]*70)

def print_board(board):
    for i in board:
        print (" ".join(i))

board_fill(board)
print_board(board)

def deszcz(board):
    x = randint(0, 69)
    y = randint(0, 69)
    z = randint(0, 69)
    board[0][x] = "*"
    board[0][y] = "*"
    board[0][z] = "*"
    while True:
        for j in range(39, 0, -1):
            board[j] = board[j-1]
        board[0] = [" "] * 70
        board[0][randint(0, 69)]="*"
        board[0][randint(0, 69)]="*"
        board[0][randint(0, 69)] = "*"
        print_board(board)
        sleep(0.2)
        clear()
deszcz(board)




