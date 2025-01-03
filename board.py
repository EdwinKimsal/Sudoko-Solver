# Import(s)
import random


# check_board function
def check_board(board):
    # Iterate through each block in board (left -> right, top -> down)
    for y in range(len(board)):
        for x in range(len(board)):
            # Check horizontal row
            if len(board[y]) > x + 1:
                if board[y][x] in board[y][x + 1:]:
                    if board[y][x] != "-":
                        return False

            # Check vertical row using temp list
            temp = []
            for i in range(len(board) - y - 1):
                if len(board[i + y + 1]) > x:
                    temp.append(board[i + y + 1][x])

            if len(board[y]) > x:
                if board[y][x] in temp:
                    if board[y][x] != "-":
                        return False

            # Check block of nine using temp list
            temp = []
            for i in range(3 - (y % 3)):
                for j in range(3 - (x % 3)):
                    if len(board[y + i]) > x + j:
                        if i != 0 or j != 0:
                                temp.append(board[y + i][x + j])

            if len(board[y]) > x:
                if board[y][x] in temp:
                    if board[y][x] != "-":
                        return False

    # If no return, board is valid
    return True


# Solve board function
def solve_board(board):
    """
    Solves the parameter board using brute force
    and returns the solved board
    """

    # Iterate through each block in the board
    for i in range(9):
        for j in range(9):

            # If it is blank, try to fill it in
            if board[i][j] == "-":
                # Set is_valid to False by default and counter to 1
                is_valid = False
                counter = 1

                print(counter)
                # Iterate while board in not legal
                while is_valid is False:
                    # Set the board space to the counter
                    board[i][j] = str(counter)

                    # Check if it is legal
                    is_valid = check_board(board)
                    print(is_valid)

                    # If is not legal, up counter
                    if is_valid is False:
                        counter += 1

    # Return the solved board
    return board


# Rand block gen function
def block_gen():
    """
    Generates three individual blocks,
    one block is one nested list and
    returns a list of lists
    """

    # Set list to a blank list of lists
    list = [[], [], []]

    # Iterate through each block and ele in each block
    for i in range(3):  # 3 blocks
        for j in range(9):  # 9 ele
            # Set is_valid to False
            is_valid = False

            # Iterate until is_valid is True
            while is_valid != True:
                num = random.randrange(1, 10)

                if num not in list[i]:
                    list[i].append(num)
                    is_valid = True

    # Return final list
    return list


# Random list (board) function
def rand_board():
    """
    Generates and returns a new random
    sudoku board
    """

    # Generate blocks
    blocks = block_gen()

    # Set list to a blank board
    list = [["-" for i in range(9)] for j in range(9)]

    # Add three separate blocks to list
    for i in range(3):
        for j in range(9):
            list[i * 3 + j // 3][i * 3 + j % 3] = blocks[i][j]

    print(check_board(list))

    # Solve the rest of the board bu calling solve_board function
    list = solve_board(list)

    # Return the final list
    return list


# Print the board function
def print_board(board):
    for row in board:
        print("-------------------------------------------------------")
        row = f"|  {"  |  ".join(row)}  |"
        print(row)

    print("-------------------------------------------------------")


# Main function
def main():
    # Generate a random list
    list = rand_board()

    #     # Set board
    #     list = [
    # [6, 2, 5, 8, 4, 3, 7, 9, 1],
    # [7, 9, 1, 2, 6, 5, 4, 8, 3],
    # [4, 8, 3, 9, 7, 1, 6, 2, 5],
    # [8, 1, 4, 5, 9, 7, 2, 3, 6],
    # [2, 3, 6, 1, 8, 4, 9, 5, 7],
    # [9, 5, 7, 3, 2, 6, 8, 1, 4],
    # [5, 6, 9, 4, 3, 2, 1, 7, 8],
    # [3, 4, 2, 7, 1, 8, 5, 6, 9],
    # [1, 7, 8, 6, 5, 9, 3, 4, 2]]

    # Set str_board
    str_board = [[str(int) for int in row] for row in list]

    # Check the board
    is_solved = check_board(list)

    print(is_solved)

    # Print the board
    print_board(str_board)


# Call main function
main()