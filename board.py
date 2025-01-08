# Import(s)
import random
import copy

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
            for i in range(3):
                for j in  range(3):
                    if 3*(y//3) + i != y and 3*(x//3) + j != x:
                        if board[3*(y//3) + i][3*(x//3) + j] != "-":
                            temp.append(board[3*(y//3) + i][3*(x//3) + j])

            if board[y][x] in temp:
                    return False

    # If no return, board is valid
    return True


# Merge solution and board function
def merge(board, solution):
    """
    Merges two parameters, board and solution,
    and returns the merged result
    """

    m_board = copy.deepcopy(board)
    count = 0

    for i in range(9):
        for j in range(9):
            if m_board[i][j] == "-":
                if count < len(solution):
                    m_board[i][j] = solution[count]
                    count += 1

    return m_board


# Solve board function
def solve_board(board):
    """
    Solves the parameter board using brute force
    and returns the solved board
    """

    solution = [1]
    is_complete = False

    while is_complete is False:
        merged_board = merge(board, solution)
        is_valid = check_board(merged_board)

        if is_valid is True:
            if len(solution) == 54:
                is_complete = True

            else:
                solution.append(1)

        else:
            solution[-1] += 1

            while solution[-1] > 9:
                solution.pop()
                solution[-1] += 1

    # Return the solved board
    return merge(board, solution)


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

    # Set str_board
    str_board = [[str(int) for int in row] for row in list]

    # Check the board
    is_solved = check_board(list)

    print(is_solved)

    # Print the board
    print_board(str_board)


# Call main function
main()