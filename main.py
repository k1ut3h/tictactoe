def new_board():
    board = [ [None, None, None], [None, None, None], [None, None, None] ]
    return board

def render(board):
    for (i, row) in enumerate(board):
        print(i, end=" ")
        print("|", end='')
        for elem in row:
            if not elem is None:
                print(elem, end=' ')
            else:
                print(" ", end=' ')
        print("|", end='')
        print("")
    print("   0 1 2")

def make_move(board, coords):
    x,y,pin = int(coords[0]), int(coords[1]), coords[2] 
    board[y][x] = pin 

def user_input():
    coords = input("Input X,Y and player-pin(O or X) (seperated by ,): ")
    coords = coords.split(",")
    return coords
    

board = new_board()
render(board)

while True:
    coords = user_input()
    if coords[0]=='exit':
        break
    if '0'<=coords[0]<='2' and '0'<=coords[1]<='2' and (coords[2]=='X' or coords[2]=='O'):
        make_move(board, coords)
        render(board)
    else:
        print("Enter valid coordinates or pin")
