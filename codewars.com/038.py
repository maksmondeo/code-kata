"""
https://www.codewars.com/kata/526dbd6c8c0eb53254000110

In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore
"""

def alphanumeric(password):
    letter = False

    for i in list(password):
        if ord(i) in range(65, 91) or ord(i) in range(97, 123):
            letter = True
        elif ord(i) in range(48, 58):
            pass
        else:
            return False

    if letter:
        return True
    return False
