"""
https://www.codewars.com/kata/51c8e37cee245da6b40000bd

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def strip_comments(strng, markers):
    lines = strng.split('\n')
    result = []

    for line in lines:
        min_index = len(line)
        for marker in markers:
            index = line.find(marker)
            if index != -1 and index < min_index:
                min_index = index
        line = line[:min_index].rstrip()
        result.append(line)

    return '\n'.join(result)
