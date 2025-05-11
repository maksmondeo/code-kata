"""
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):
    l = list(message)
    for i in range(len(l)):
        if ord(l[i]) >= 65 and ord(l[i]) <= 77 or ord(l[i]) >= 97 and ord(l[i]) <= 109:
            l[i] = chr(ord(l[i]) + 13)
        else:
            if ord(l[i]) > 77 and ord(l[i]) <= 90:
                print(ord(l[i]))
                l[i] = chr(64 + 13 - (90 - ord(l[i])))
            elif ord(l[i]) > 109 and ord(l[i]) <= 122:
                l[i] = chr(96 + 13 - (122 - ord(l[i])))
    return("".join(l))
