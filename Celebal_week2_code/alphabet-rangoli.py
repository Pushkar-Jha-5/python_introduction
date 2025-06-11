#pattern printing with the help of alphabets
import string

def print_rangoli(size):
    # Get lowercase alphabets
    alphabet = string.ascii_lowercase

    # Create the pattern
    lines = []
    for i in range(size):
        # Create left and right parts
        left = alphabet[size-1:i:-1]
        right = alphabet[i:size]
        line = '-'.join(left + right)

        # Center align with '-'
        lines.append(line.center(4*size-3, '-'))

    # Print the full rangoli
    print('\n'.join(lines[::-1] + lines[1:]))

# Take user input
n = int(input("Enter the size of Rangoli (1-26): "))
print_rangoli(n)
