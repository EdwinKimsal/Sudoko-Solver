# Import(s)
import random

# Random list function
def rand_board(square_len, min_num, max_num):
    # Set a blank list
    list = []

    # Iterate for square_len times
    for x in range(square_len):
        # Append a list of square_len nums
        list.append([str(random.randint(min_num, max_num)) for num in range(square_len)])

    # Iterate through each block
    for i in range(len(list)):
        for j in range(len(list[i])):
            # Make 0s spaces
            if list[i][j] == "0":
                list[i][j] = " "

    # Return the final list
    return list


# check_board function
def check_board(board):
    for y in range(len(board)):
        for x in range(len(board) - 1):
            if board[y][x] in board[y][x+1:]:
                return False


# Print the board function
def print_board(board):
    for row in board:

        print("-------------------------------------------------------")
        row = f"|  {"  |  ".join(row)}  |"
        print(row)

    print("-------------------------------------------------------")


# Main function
def main():
    # # Generate a random list
    # list = rand_board(9, 0, 9)

    # Set board
    list = [
[6, 2, 5, 8, 4, 3, 7, 9, 1],
[7, 9, 1, 2, 6, 5, 4, 8, 3],
[4, 8, 3, 9, 7, 1, 6, 2, 5],
[8, 1, 4, 5, 9, 7, 2, 3, 6],
[2, 3, 6, 1, 8, 4, 9, 5, 7],
[9, 5, 7, 3, 2, 6, 8, 1, 4],
[5, 6, 9, 4, 3, 2, 1, 7, 8],
[3, 4, 2, 7, 1, 8, 5, 6, 9],
[1, 7, 8, 6, 5, 9, 3, 4, 2]]

    # Set str_board
    str_board = [[str(int) for int in row] for row in list]

    # Check the board
    is_solved = check_board(list)

    print(is_solved)

    # Print the board
    print_board(str_board)

# Call main function
main()