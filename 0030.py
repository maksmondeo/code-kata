"""
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
"""

def calc(digit, digit2, operator):
    match operator:
        case "plus":
            return digit + digit2
        case "minus":
            print(digit, digit2)
            return digit - digit2
        case "times":
            return digit * digit2
        case "div":
            return digit // digit2

def zero(*args):
    if args:
        return calc(0, args[0][0], args[0][1])
    return 0

def one(*args):
    if args:
        return calc(1, args[0][0], args[0][1])
    return 1

def two(*args):
    if args:
        return calc(2, args[0][0], args[0][1])
    return 2

def three(*args):
    if args:
        return calc(3, args[0][0], args[0][1])
    return 3

def four(*args):
    if args:
        return calc(4, args[0][0], args[0][1])
    return 4

def five(*args):
    if args:
        return calc(5, args[0][0], args[0][1])
    return 5


def six(*args):
    if args:
        return calc(6, args[0][0], args[0][1])
    return 6


def seven(*args):
    if args:
        return calc(7, args[0][0], args[0][1])
    return 7


def eight(*args):
    if args:
        return calc(8, args[0][0], args[0][1])
    return 8


def nine(*args):
    if args:
        return calc(9, args[0][0], args[0][1])
    return 9


def plus(digit):
    return digit, "plus"

def minus(digit):
    return digit, "minus"

def times(digit):
    return digit, "times"

def divided_by(digit):
    return digit, "div"
