#!/usr/bin/env python3
"""Solution to Python Challenge #7

Start: http://www.pythonchallenge.com/pc/def/oxygen.html

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
