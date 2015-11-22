#!/usr/bin/env python3
"""
Solution to Python Challenge #11.

Start: http://www.pythonchallenge.com/pc/return/5808.html

The start page has a picture in it (URL below).  It looks rather fuzzy, and the
title of the page mentions odd and even.  This gives me the idea that there are
two images "phased" together somehow.  If you zoom in, you can see a
checkerboard pattern confirming this.  So, you get your imaging library, and
split it into the four images corresponding to the four blocks of the
checkerboard.  Turns out there were just two images, each duplicated twice.
The darker one says "evil", which is the key to the next level.  This is
another one I had to hard code the ending to, but at least I get to display the
answer first.
"""

import webbrowser
from io import BytesIO

import requests
from PIL import Image

IMG_URL = r'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'
URL = r'http://huge:file@www.pythonchallenge.com/pc/return/%s.html'


def main():
    response = requests.get(IMG_URL)

    image = Image.open(BytesIO(response.content))
    image_pixels = image.load()

    width, height = image.size

    xodd = Image.new('RGB', (width//2, height//2))
    xodd_pixels = xodd.load()

    yodd = Image.new('RGB', (width//2, height//2))
    yodd_pixels = yodd.load()

    bothodd = Image.new('RGB', (width//2, height//2))
    bothodd_pixels = bothodd.load()

    even = Image.new('RGB', (width//2, height//2))
    even_pixels = even.load()

    for x in range(width):
        for y in range(height):
            if x % 2 == 1 and y % 2 == 1:
                bothodd_pixels[x//2, y//2] = image_pixels[x, y]
            elif x % 2 == 1:
                xodd_pixels[x//2, y//2] = image_pixels[x, y]
            elif y % 2 == 1:
                yodd_pixels[x//2, y//2] = image_pixels[x, y]
            else:
                even_pixels[x//2, y//2] = image_pixels[x, y]

    bothodd.show()
    xodd.show()
    yodd.show()
    even.show()

    webbrowser.open(URL % 'evil')


if __name__ == '__main__':
    main()
