# Import(s)
import random

# check_board function
def check_board(board):
    # Iterate through each block in board (left -> right, top -> down)
    for y in range(len(board)):
        for x in range(len(board)):
            # Check horizontal row
            if len(board[y]) > x+1:
                if board[y][x] in board[y][x+1:]:
                    return False

            # Check vertical row using temp list
            temp = []
            for i in range(len(board) - y - 1):
                if len(board[i + y + 1]) > x:
                    temp.append(board[i + y + 1][x])

            if len(board[y]) > x:
                if board[y][x] in temp:
                    return False

            # Check block of nine using temp list
            temp = []
            for i in range(3 - (y % 3)):
                for j in range(3 - (x % 3)):
                    if len(board[y+i]) > x + j:
                        if i != 0 or j != 0:
                            temp.append(board[y+i][x+j])

            if len(board[y]) > x:
                if board[y][x] in temp:
                    return False

    # If no return, board is valid
    return True


# Random list function
def rand_board():
    # Set a blank temp and list
    list = [[],[],[],[],[],[],[],[],[]]

    # Iterate for square_len times
    for y in range(9):
        for x in range(9):
            isValid = False

            while isValid == False:
                num = str(random.randrange(1, 10))
                list[y].append(num)
                print(list)

                isValid = check_board(list)
                print(isValid)

                if isValid == False:
                    list[y].pop(-1)

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