def display_board(board):
    output =""
    for i in range(0,9):
        output += str(board[i])
        if (i+1) % 3 != 0:
            output += "|"
        if (i+1) % 3 == 0 and i + 1 != 9:
            output += "\n-+-+-\n"
    print (output)

def move(board, is_x):
    number_input = 0
    mark = ""
    if is_x:
        number_input =  int(input("x's turn to choose a square (1-9): "))
        mark = "x"
    else:
        number_input =  int(input("o's turn to choose a square (1-9): "))
        mark = "o"
    
    board[number_input-1] = mark
    return  not is_x

def check_win(board):
    won = False
    if board[0] == board[1] and board[1] == board[2]:
        won = True
    if board[3] == board[4] and board[4] == board[5]:
        won = True
    if board[6] == board[7] and board[7] == board[8]:
        won = True
    if board[0] == board[4] and board[4] == board[8]:
        won = True
    if board[2] == board[4] and board[4] == board[6]:
        won = True
    if board[0] == board[3] and board[3] == board[6]:
        won = True
    if board[1] == board[4] and board[4] == board[7]:
        won = True
    if board[2] == board[5] and board[5] == board[8]:
        won = True
    return won
def game():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_x = True
    while not check_win(board):
        display_board(board)
        is_x = move(board, is_x)
    display_board(board)
    print("Good game. Thanks for playing!")

game()
        



