#Task to wrap the string into a paragraph of given width 
import textwrap

# Take input from the user
text = input("Enter the string: ")
width = int(input("Enter the width: "))

# Wrap the text
wrapped_text = textwrap.fill(text, width)

# Output
print("\nWrapped Paragraph:")
print(wrapped_text)
