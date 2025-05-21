"""
https://www.codewars.com/kata/526989a41034285187000de4

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
Examples

* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
"""

def address(ip):
    l = ip.split(".")
    result = int(l[3]) + int(l[2]) * 256 + int(l[1]) * 256**2 + int(l[0]) * 256**3
    return result


def ips_between(start, end):
    return address(end) - address(start)
