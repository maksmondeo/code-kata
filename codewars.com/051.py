"""
https://www.codewars.com/kata/517abf86da9663f1d2000003

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    if "-" not in text and "_" not in text:
        return text

    result = text[0]
    first = False

    for i in range(1, len(text)):
        if first:
            result += text[i].capitalize()
            first = False
        elif text[i] == "_" or text[i] == "-":
            first = True
        else:
            result += text[i]
    return result

