# Calculate the avarges of items present inside a python set
def average_of_set(s):
    if not s:
        return 0  # Return 0 if the set is empty
    return sum(s) / len(s)

# Take input from the user
input_string = input("Enter numbers separated by spaces: ")

# Convert the input string to a set of integers
number_set = set(map(int, input_string.split()))

avg = average_of_set(number_set)

print("Average of the set is:", avg)
