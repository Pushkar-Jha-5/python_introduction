#Task to make the first letter of every words as capital
def format_name(name):
    # Split the name into words (e.g., first and last name)
    words = name.strip().split()
    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]
    # Join the capitalized words back into a single string
    return ' '.join(capitalized_words)

input_name = input("Enter the full name: ")
formatted_name = format_name(input_name)
print("Formatted name for passport:", formatted_name)
