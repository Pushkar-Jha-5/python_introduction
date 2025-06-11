#Split a string into equal parts of length and Convert each parts by removing any subsequent occurrences of non-distinct
def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        substring = string[i:i + k]
        seen = ''
        for char in substring:
            if char not in seen:
                seen += char
        print(seen)

# Example usage:
s = input("Enter the string: ")
k = int(input("Enter the value of k (factor of length of string): "))
merge_the_tools(s, k)
