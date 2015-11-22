#!/usr/bin/env python3
"""
Solution to Python Challenge #14.

Start: http://www.pythonchallenge.com/pc/return/italy.html

The image shows a cinnabun, suggesting a spiral pattern.  There is another
linked image that has size 10000x1.  They reshaped the image to 100x100 in the
page, suggesting that we might want to reshape the image in a different way
(say a spiral) in the 100x100 frame.  So, I wrote a loop to drop pixels in a
decreasing spiral, and what do you know, I got a cat.  Its name is uzi.
"""

import webbrowser
from io import BytesIO

import requests
from PIL import Image

URL = 'http://huge:file@www.pythonchallenge.com/pc/return/%s.html'
PIC = 'http://huge:file@www.pythonchallenge.com/pc/return/wire.png'


def main():
    response = requests.get(PIC)
    wire = Image.open(BytesIO(response.content))
    wire_pixels = wire.load()

    idx = 0
    cinnabun = Image.new('RGB', (100, 100))
    cinnabun_pixels = cinnabun.load()

    left, right, top, bottom = 0, 99, 0, 99
    while idx < 10000:
        # Start at top right and go down.
        for i in range(top, bottom+1, 1):
            cinnabun_pixels[right, i] = wire_pixels[idx, 0]
            idx += 1
        right -= 1
        # Now, bottom right to bottom left
        for i in range(right, left-1, -1):
            cinnabun_pixels[i, bottom] = wire_pixels[idx, 0]
            idx += 1
        bottom -= 1
        # Now, bottom left to top left
        for i in range(bottom, top-1, -1):
            cinnabun_pixels[left, i] = wire_pixels[idx, 0]
            idx += 1
        left += 1
        # Now, top left to top right
        for i in range(left, right+1, 1):
            cinnabun_pixels[i, top] = wire_pixels[idx, 0]
            idx += 1
        top += 1

    cinnabun.show()
    webbrowser.open(URL % 'cat')
    webbrowser.open(URL % 'uzi')


if __name__ == '__main__':
    main()
