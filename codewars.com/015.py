"""
https://www.codewars.com/kata/513e08acc600c94f01000001

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

def rgb(r, g, b):
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255

    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0

    red = hex(r)[2:].upper()
    if len(red) == 1:
        red = "0" + red
    print(red)

    green = hex(g)[2:].upper()
    if len(green) == 1:
        green = "0" + green
    print(green)

    blue = hex(b)[2:].upper()
    if len(blue) == 1:
        blue = "0" + blue
    print(blue)

    return red + green + blue
