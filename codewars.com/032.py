"""
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""

def first_non_repeating_letter(s):
    banned = []
    result = ""
    low = s.lower()

    for i in low:
        if i not in result and i not in banned:
            result += i
        elif i not in banned:
            result = result.replace(i, "")
            banned.append(i)

    if result[:1].islower() and result[:1].upper() in s:
        if result[:1] not in s:
            return result[:1].upper()
        elif s.index(result[:1]) < s.index(result[:1].upper()):
            return result[:1]
        return result[:1].upper()

    if result[:1].isupper() and result[:1].lower() in s:
        if result[:1] not in s:
            return result[:1].lower()
        elif s.index(result[:1]) < s.index(result[:1].lower()):
            return result[:1]
        return result[:1].lower()

    return result[:1]
