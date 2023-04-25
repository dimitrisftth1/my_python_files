board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
player = "O"

for _ in range(9):
    print("  +---+---+---+")
    print(str(2) + " |" + board[2][0] + "  | " + board[2][1] + " | " + board[2][2] + " |" )
    print("  +---+---+---+")
    print(str(1) + " |" + board[1][0] + "  | " + board[1][1] + " | " + board[1][2] + " |" )
    print("  +---+---+---+")
    print(str(0) + " |" + board[0][0] + "  | " + board[0][1] + " | " + board[0][2] + " |" )
    print("  +---+---+---+")
    print("    0   1   2")

    #choose next player
    if player == "X":
        player = "O"
    else:
        player = "X"

    #user input
    while True:
        print("Player " + player + " plays!")
        row = int(input("Give row: "))
        col = int(input("Give column: "))
        if row < 0 or row > 2 :
            print("Row out of bounds  (0-2). ")
            continue
        elif col < 0 or col > 2:
            print("Column out of bounds  (0-2). ")
            continue
        else:
            board[row][col] = player
            break
    # check winner
    winner = False
    if (board[0][0] == board[0][1] and board[0][1] == board[1][1]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != " ":
        winner = player
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]) and board[0][0] != " ":
        winner = player
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]) and board[0][1] != " ":
        winner = player
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]) and board[0][2] != " ":
        winner = player
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[0][2] != " ":
        winner = player

    if winner:
        print("  +---+---+---+")
        print(str(2) + " |" + board[2][0] + "  | " + board[2][1] + " | " + board[2][2] + " |")
        print("  +---+---+---+")
        print(str(1) + " |" + board[1][0] + "  | " + board[1][1] + " | " + board[1][2] + " |")
        print("  +---+---+---+")
        print(str(0) + " |" + board[0][0] + "  | " + board[0][1] + " | " + board[0][2] + " |")
        print("  +---+---+---+")
        print("Player " + player + " Won! ")
        break
    else:
        print("  +---+---+---+")
        print(str(2) + " |" + board[2][0] + "  | " + board[2][1] + " | " + board[2][2] + " |")
        print("  +---+---+---+")
        print(str(1) + " |" + board[1][0] + "  | " + board[1][1] + " | " + board[1][2] + " |")
        print("  +---+---+---+")
        print(str(0) + " |" + board[0][0] + "  | " + board[0][1] + " | " + board[0][2] + " |")
        print("  +---+---+---+")
        print("Isopalia! ")