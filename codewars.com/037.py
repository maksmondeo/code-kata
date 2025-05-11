"""
https://www.codewars.com/kata/54a91a4883a7de5d7800009c

Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

def increment_string(strng):
    if not strng[-1:].isdigit():
        return strng + "1"

    index = len(strng)
    while index > 0 and strng[index - 1].isdigit():
        index -= 1

    number_str = strng[index:]

    number_len = len(number_str)
    incremented = str(int(number_str) + 1)
    incremented = incremented.zfill(number_len)

    return strng[:index] + incremented
