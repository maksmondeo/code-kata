"""
https://www.codewars.com/kata/5324945e2ece5e1f32000370/python

Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""

def sum_strings(x, y):
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"

    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))

    if carry:
        result.append(str(carry))

    return "".join(reversed(result))
