"""
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html
Examples
N 	Product 	N factorial 	Trailing zeros
6 	1*2*3*4*5*6 	720 	1
12 	1*2*3*4*5*6*7*8*9*10*11*12 	479001600 	2

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""

from math import floor, log

def zeros(n):
    if n==0:
        return 0
    
    result = 0
    for i in range(1, floor(log(n, 5) + 1)):
        result += floor(n/5**i)
    
    return result
