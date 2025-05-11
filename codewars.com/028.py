"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    l = text.split(" ")
    result = ""
    for i in l:
        if len(i) == 1:
            if ord(i) == 33 or ord(i) == 63:
                result += i
                continue
        result += i[1:] + i[:1] + "ay "

    if result[-1] == " ":
        return result[:-1]
    return result
