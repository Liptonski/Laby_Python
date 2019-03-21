# animacja jakiegos tam kwadratu nie wiem w sumie

from time import sleep

def clear():
    print("\033[2J")

board=[]
rows=int(input("Podaj nieparzysta ilosc wierszy: "))
cols=int(input("Podaj nieparzysta ilosc kolumn: "))
rows_mid=rows//2
cols_mid=cols//2
size=0
mark=1

def board_fill(board):
    for i in range(0, rows):
        board.append(["0"]*cols)

def print_board(board):
    for i in board:
        print (" ".join(i))

def square(tab, c, size):
    for i in range(-size, size+1):
        for j in range(-size, size+1):
            tab[rows_mid+i][cols_mid+j]=c

board_fill(board)
#print_board(board)

z=1
while True:
    if size==0:
        board[rows_mid][cols_mid]="="
        size=1
    elif mark==-1:
        square(board, "=", size-1)
        square(board, "O", size)
        size+=mark
    else:
        square(board, "=", size)
        square(board, "O", size-1)
        size += mark
    print_board(board)

    if size == 0 or size == min(rows_mid, cols_mid):
        mark *= -1
    sleep(1)
    clear()

