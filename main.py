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

def make_move(board, coords, pin):
    x,y = int(coords[0]), int(coords[1]) 
    new_board = board
    new_board[y][x] = pin 
    return new_board

def user_input():
    coords = input("Input X,Y(seperated by ,): ")
    coords = coords.split(",")
    return coords
    
def has_won(board):
    all_line_co_ords = get_all_line_co_ords()

    for line in all_line_co_ords:
        line_values = [board[x][y] for (x,y) in line]
        if len(set(line_values)) ==1 and line_values[0] is not None:
            return True 
    return False 

def get_all_line_co_ords():
    cols = []
    for x in range(0, 3):
        col = []
        for y in range(0, 3):
            col.append((x,y))
        cols.append(col)
    rows = []
    for x in range(0, 3):
        row = []
        for y in range(0, 3):
            row.append((x,y))
        rows.append(row)
    diagonals = [
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
            ]
    return cols+rows+diagonals

board = new_board()
render(board)

i = 0

while True:
    pin = '' 
    if i%2==0:
        pin = 'X'
        print("X's turn")
    else:
        pin = 'O'
        print("O's turn");
    i+=1
    coords = user_input()
    if coords[0]=='exit':
        break
    if len(coords)==2:
        if '0'<=coords[0]<='2' and '0'<=coords[1]<='2':
            old_board = board
        new_board = make_move(old_board, coords, pin)
        render(new_board)
        if has_won(new_board):
            print("Congratulations {winner}, you won!".format(winner=pin))
            break
        old_board = new_board
    else:
        print("Enter valid coordinates or pin, on your next turn")
