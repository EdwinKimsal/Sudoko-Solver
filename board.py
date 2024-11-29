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
    list = rand_board(9, 0, 9)

    # Print the board
    print_board(list)

# Call main function
main()