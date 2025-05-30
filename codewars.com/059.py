"""
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    if not s:
        return []
    
    l = [""]
    for i in s:
        if len(l[-1]) < 2:
            l[-1] += i
        else:
            l.append(i)

    if len(s) % 2:
        l[-1] = l[-1] + "_"
    return l
