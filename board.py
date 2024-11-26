# Import(s)
import random

# Random list function
def rand_list(square_len, min_num, max_num):
    # Set a blank list
    list = []

    # Iterate for square_len times
    for x in range(square_len):
        # Append a list of square_len nums
        list.append([random.randint(min_num, max_num) for num in range(square_len)])

    # Return the final list
    return list


# Main function
def main():
    # Generate a random list
    list = rand_list(9, 1, 9)

    # Print the list
    print(list)

# Call main function
main()