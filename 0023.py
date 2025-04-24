"""
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

def generate_hashtag(s):
    l = list(s)
    check = True
    for i in range(len(l)):
        if check:
            l[i] = l[i].upper()
        if l[i] == " ":
            check = True
        elif not check:
            l[i] = l[i].lower()
            check = False
        else:
            check = False

    l = "".join(l)

    result = "#" + l
    result = result.replace(" ", "")
    
    if len(l)>=139 or result == "#":
        return False
    return result
