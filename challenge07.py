#!/usr/bin/env python3
"""Solution to Python Challenge #7

Start: http://www.pythonchallenge.com/pc/def/oxygen.html

The strip of greyscale blocks in the image contains information.  Grey color has
R=G=B, and the values are between 0 and 255.  Coincidentally, this can hold
exactly one ASCII character of data.  The strip of grey in the image has 7 pixel
wide blocks.  It starts at column 0 and ends at column 608.  It occurs around
row 47.  Using that information, you can sample one pixel from each block, get
the color value for each pixel, and get an ASCII character from that.  This
allows you to build a string from the strip.

However, that's not all.  The string has a complement, followed by a list of
numbers, each of which code for a character in the final level name.  So, you
need to convert those to a string, and then you have the name of the next level.

This process could be done without pypng.  You'd need to use the color sampling
tool on your image editor of choice.  But using a library like pypng allows me
to automate it so that this solution runs just like any other one.

"""

import webbrowser
from urllib.request import urlopen
import re
import png


def main():
    # Open image and read its rows.
    img = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    reader = png.Reader(file=urlopen(img))
    result_tuple = reader.read()
    rows = list(result_tuple[2])

    # Row 47 is in the grey strip.  Each pixel is 4 bytes (RGB, transparency),
    # each cell is 7 wide, and the strip ends at column 608.
    row = rows[47]  # this row is in the grey strip
    string = ''.join(chr(row[c]) for c in range(0, 608*4, 7*4))
    print(string)

    # Get each number and construct string for next level
    level = ''.join(chr(int(num)) for num in re.findall(r'\d+', string))
    print(level)

    # YUSSSS!
    webbrowser.open('http://www.pythonchallenge.com/pc/def/%s.html' % level)


if __name__ == '__main__':
    main()
