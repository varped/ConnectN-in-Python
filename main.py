"""
This program plays the game Connect-N that has two players.
Each player takes a turn dropping one of their pieces into a column and
the game ends if either player get n pieces in a row or the board becomes full.
"""

def get_input(prompt: str) -> int:
    """
    This function asks the user for the input and checks if the input is valid.
    :param prompt: str
    :return: int
    """
    user_input = input(prompt)
    while not user_input.isdigit() or int(user_input) <= 0:
        user_input = input(prompt)
    return int(user_input)

def get_number_of_rows_and_columns():
    """
    This function uses the get_input function to ask the user
    for the number of rows and columns to create the board.
    """
    num_rows = get_input("Enter the number of rows: ")
    num_cols = get_input("Enter the number of columns: ")
    return num_rows, num_cols

def get_number_of_pieces_needed_to_win(num_rows: int, num_cols: int, num_of_pieces: int):
    """
    This function asks the user for an input on the number of pieces needed in a row to win.
    :param: num_rows: int
    :param: num_cols: int
    :param: num_of_pieces: int
    :return: int
    """
    while not num_of_pieces.isdigit() or int(num_of_pieces) <= 0:
        num_of_pieces = input("Enter the number of pieces in a row to win: ")

    num_of_pieces = int(num_of_pieces)

    if num_of_pieces > num_cols and num_cols > num_rows:
        num_of_pieces = num_cols
    elif num_of_pieces > num_rows and num_rows > num_cols:
        num_of_pieces = num_rows
    return num_of_pieces

def make_board(num_rows: int, num_cols: int, blank_char: str) -> list:
    """
    Make a board that is number of rows by number of columns big that
    is filled with blank_characters
    :param num_rows:
    :param num_cols:
    :param blank_char:
    :return: list
    """
    board = []
    for row_number in range(num_rows):
        row = [blank_char] * num_cols
        board.append(row)
    return board

def display_game_state(board: list) -> None:
    """
    This function will display the state of the game and the board to the user as they play.
    :param board: list
    :return:
    """
    print(end='  ')
    for col_num in range(len(board[0])):
        print(col_num, end=' ')
    print()

    for row_num, row in reversed(list(enumerate(board))):
        print(row_num, end=' ')
        print(' '.join(row))

def check_win(board, player, num_of_pieces):
    """
        This function will check if someone won the game.
        :return:
        """
    return win_horz(board, player, num_of_pieces) or \
        win_vert(board, player, num_of_pieces) or \
        win_diagonally(board, player, num_of_pieces)
def win_horz(board, player, num_of_pieces) -> bool:
    """
    This function checks if the user won horizontally.
    :param board: list
    :param player: int
    :param num_of_pieces: int
    :return: bool
    """
    for row in board:
        count = 0
        for space in row:
            if space == player:
                count += 1
                if count == num_of_pieces:
                    return True
            else:
                count = 0
    return False

def win_vert(board, player, num_of_pieces) -> bool:
    """
    This function checks if the user won vertically.
    :param board: list
    :param player: int
    :param num_of_pieces: int
    :return: bool
    """
    for i in range(len(board[0])):
        count = 0
        for j in range(len(board)):
            if board[j][i] == player:
                count += 1
                if count == num_of_pieces:
                    return True
            else:
                count = 0
    return False

def win_diagonally(board, player, num_of_pieces) -> bool:
    """
    This function checks if the user won diagonally (both right and left)
    X
     X
      X
    or
       X
      X
    X
    :param board: list
    :param player: int
    :param num_of_pieces: int
    :return: bool
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                if i + num_of_pieces <= len(board) and j + num_of_pieces <= len(board[0]):
                    count = 0
                    for k in range(num_of_pieces):
                        if board[i + k][j + k] == player:
                            count += 1
                            if count == num_of_pieces:
                                return True

                if i + num_of_pieces <= len(board) and j - num_of_pieces + 1 >= 0:
                    count = 0
                    for k in range(num_of_pieces):
                        if board[i + k][j - k] == player:
                            count += 1
                            if count == num_of_pieces:
                                return True
    return False

def tie(board, blank_space) -> bool:
    """
    This function checks if there is a tie in the game.
    :param board: list
    :param blank_character: str
    :return: bool
    """
    if check_win(board, blank_space, 1):
        return False

    for row in board:
        for piece in row:
            if piece == blank_space:
                return False
    return True

def all_same(board, blank_space) -> bool:
    """
    This function checks if the board is full and all the spaces are filled.
    :param board: list
    :param blank_space: str
    :return: bool
    """
    for row in board:
        for space in row:
            if space == blank_space:
                return False
    return True

def get_player_move(board: list, num_rows, blank_space: str) -> int:
    """
    This function gets a valid move from the user.
    :param board: list
    :param num_cols
    :param blank_space: str
    :return: int
    """
    while True:
        user_move = input('Enter the column you want to play in: ')
        if user_move.isdigit():
            col = int(user_move)
            if 0 <= col < len(board[0]) and board[num_rows - 1][col] == blank_space:
                return col

def next_open_row(board, col, num_rows, blank_space):
    for row in range(num_rows):
        if board[row][col] == blank_space:
            return row

def update_game_state(piece, col, board, row) -> list:
    """
    This function will update the game state after a player's move.
    :param piece: str
    :param col: int
    :param board: list
    :return: list
    """
    board[row][col] = piece
    return board

def change_turn(current_player_turn: int):
    """
    This function changes the player turn.
    :param turn: int
    :return: int
    """
    if current_player_turn == 0:
        return 1
    else:
        return 0

def play_connect_n():
    blank_space = '*'
    num_rows, num_cols = get_number_of_rows_and_columns()
    num_of_pieces = input("Enter the number of pieces in a row to win: ")
    num_of_pieces = get_number_of_pieces_needed_to_win(num_rows, num_cols, num_of_pieces)
    board = make_board(num_rows, num_cols, blank_space)
    pieces = ['X', 'O']
    current_player = 0
    display_game_state(board)

    while not check_win(board, pieces[current_player], num_of_pieces) and not tie(board, blank_space):
        user_move = get_player_move(board, num_rows, blank_space)
        row = next_open_row(board, user_move, num_rows, blank_space)
        board = update_game_state(pieces[current_player], user_move, board, row)
        display_game_state(board)
        if check_win(board, pieces[current_player], num_of_pieces):
            declare_winner(current_player, board, blank_space)
            break
        if tie(board, blank_space):
            print('Tie Game')
            break
        current_player = change_turn(current_player)

def declare_winner(current_player: int, board: list, blank_space: str) -> None:
    if current_player == 0:
        print('Player 1 won!')
    elif current_player == 1:
        print('Player 2 won!')
    else:
        print('Tie Game')

play_connect_n()
