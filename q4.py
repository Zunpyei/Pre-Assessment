def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    rev = ""
    if(type(s) == str):
        totallen = len(s)
        index = totallen - 1
        for i,char in enumerate (s):
            rev += s[index-i]
    return rev


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))
print(string_reverse("Python"))
