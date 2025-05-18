"""
https://www.codewars.com/kata/54d512e62a5e54c96200019e

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

def prime_factors(n):
    result = ""
    for i in range(2, n + 1):
        count = 0
        while n % i == 0:
            count += 1
            n /= i

        if count > 1:
            result += f"({i}**{count})"
        elif count == 1:
            result += f"({i})"
            
        if n == 1:
            return result
