import os  # the new import statement

# board = [str(i + 1) for i in range(9)]
# board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
# print(board)


def initialize_board():
    board = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    return board


def display_board(board):
    # print the board in 3x3 format
    board_formatted = f"""
      |{board[1]}|{board[2]}|{board[3]}|
      |{board[4]}|{board[5]}|{board[6]}|
      |{board[7]}|{board[8]}|{board[9]}|
    """  # the board content
    print(board_formatted)


def update_board(board, player, position):
    """
    board: dict
    player: integers, 1 or 2
    position: integers, between 1 and 9
    """
    # mark = 'X'
    # if player == 2:
    #     mark = 'O'
    mark = "X" if player == 1 else "O"

    # update the board
    if board[position] in ["X", "O"]:
        print("Position possessed!!")
    else:
        board[position] = mark


def check_winner(board, position):
    if board[position] == "X":
        return 1
    else:
        return 2


def check_win(board):
    winner = -1
    # rows: i could be 1,4,7
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] and board[i] == board[i + 2]:
            winner = check_winner(board=board, position=i)
            return winner

    # columns
    for i in range(1, 4):
        if board[i] == board[i + 3] and board[i] == board[i + 6]:
            winner = check_winner(board=board, position=i)
            return winner

    # diagonals
    if (board[1] == board[5] and board[1] == board[9]) or (
        board[3] == board[5] and board[3] == board[7]
    ):
        winner = check_winner(board=board, position=5)
        return winner

    return winner  # -1


def check_tie(board):
    for i in range(1, 10):
        if board[i] not in ["X", "O"]:
            return False
    return True


def check_valid_input(input):
    pass


def play():
    print(f"Welcome to the tic tac toe game!! Here are the rules:")
    print("1. There will be 2 players playing")
    print("2. In each move, type in a desired position to fill")
    # initialize the board
    board = initialize_board()
    # display the board
    display_board(board=board)
    player = 1
    quit_command = ["q", "Q"]
    reset_command = ["r", "R", "reset"]

    while True:
        # collect an input
        # position = int(
        #     input(f"Player {player} is playing, input a position to fill:\n")
        # )

        user_input = input(
            f"Player {player} is playing, input a position 1-9 to fill:\n"
        )

        # define q means quit the game, r means reset the game
        if user_input in quit_command:
            print("Game END")
            break

        if user_input in reset_command:
            board = initialize_board()
            print("Board Reinitialized!")
            continue

        # if user_input in quit_command:
        #     flg_quit = input("Are you sure to quit the game? (y/n)")
        #     if flg_quit == "y":
        #         break
        #     else:
        #         user_input = input(
        #             f"Player {player} is playing, input a position 1-9 to fill:\n"
        #         )
        #         if not (user_input in "123456789" and len(user_input) == 1):
        #             print("Invalid input, please try again!!")
        #             continue

        # option 1 to check input:
        # if not (
        #     user_input.isnumeric() and int(user_input) >= 1 and int(user_input) <= 9
        # ):  # not a valid input
        #     print("Invalid input, please try again!!")
        #     continue

        # option 2 to check input:
        if not (user_input in "123456789" and len(user_input) == 1):
            print("Invalid input, please try again!!")
            continue

        position = int(user_input)
        # update the board
        update_board(board=board, player=player, position=position)
        os.system("cls" if os.name == "nt" else "clear")  # the new line added

        # display the board
        display_board(board=board)

        # check win
        winner = check_win(board=board)
        if winner in [1, 2]:
            print(f"Player {winner} wins!! Congrats!!")
            return

        # check tie
        tie = check_tie(board=board)
        if tie:
            print(f"It is a tie!!")
            return

        player = 2 if player == 1 else 1


play()
