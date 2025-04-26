"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(lst):
    indexes = []
    for i in range(len(lst)):
        if lst[i] == 0:
            indexes.append(i)
    
    count = 0
    for i in indexes:
        lst.pop(i-count)
        count += 1
    
    for i in range(count):
        lst.append(0)
    
    return lst
