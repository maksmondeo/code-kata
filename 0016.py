"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/solutions/python

Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

"""

def snail(snail_map):
    limit = len(snail_map)
    x = 0
    y = 0
    result = []
    dir = "r"
    bound = 0

    for i in range(len(snail_map) * len(snail_map[0])):
        result.append(snail_map[y][x])

        if dir == "r":
            x += 1
            if x + bound + 1 == limit:
                dir = "d"

        elif dir == "d":
            y += 1
            if y + bound + 1 == limit:
                dir = "l"

        elif dir == "l":
            x -= 1
            if x - bound == 0:
                dir = "u"

        elif dir == "u":
            y -= 1
            if y - bound - 1 == 0:
                dir = "r"
                bound += 1

    return result

