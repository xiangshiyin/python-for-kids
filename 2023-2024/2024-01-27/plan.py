import os

def print_board_static():
    "For a tic-tac-toe board, print it out."
    print("""
          |1|2|3|
          |4|5|6|
          |7|8|9|
          """)

def print_board_dynamic(board):
    print(f"""
          |{board[1]}|{board[2]}|{board[3]}|
          |{board[4]}|{board[5]}|{board[6]}|
          |{board[7]}|{board[8]}|{board[9]}|
          """)

def update_board(board, player, position):
    board[position] = "X" if player == 1 else "O"

def check_win(board):
    # Check rows
    for i in range(1, 10, 3):
        if board[i] == board[i+1] == board[i+2]:
            return True
    # Check columns
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6]:
            return True
    # Check diagonals
    if board[1] == board[5] == board[9]:
        return True
    if board[3] == board[5] == board[7]:
        return True
    return False

def check_tie(board):
    for i in range(1, 10):
        if board[i] != "X" and board[i] != "O":
            return False
    return True

def play_game():
    board = {i: str(i) for i in range(1, 10)}
    player = 1
    while True:
        print_board_dynamic(board)
        position = int(input(f"Player {player}, enter a position: "))
        update_board(board, player, position)
        os.system("cls" if os.name == "nt" else "clear")

        if check_win(board):
            print(f"Player {player} wins!")
            print_board_dynamic(board)
            break
        if check_tie(board):
            print("It's a tie!")
            print_board_dynamic(board)
            break
        player = 1 if player == 2 else 2


if __name__ == "__main__":
    play_game()
