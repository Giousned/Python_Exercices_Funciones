multy = lambda x, y: x * y
print(multy(2,2))

rapid = lambda str: str[:-1]


# From this line above, plese do not change code below
print(rapid("bob")) #should print bo


# https://careerkarma.com/blog/python-remove-character-from-string/

# Remove Last Character from String
# To remove the last character from a string, use the [:-1] slice notation.
# This notation selects the character at the index position -1 (the last character in a list).
# Then, the syntax returns every character except for that one.

# The syntax for removing the last character from a string is:
# your_string = "A string"
# print(your_string[:-1])