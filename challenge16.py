#!/usr/bin/env python3
"""
Solution to Python Challenge #16.

Start: http://www.pythonchallenge.com/pc/return/mozart.html

The picture is a "static-y" image, and if you examine it closely, you can see
that each row of pixels contains a strip of magenta at some point. Since the
title of the page says "let's get this straight", you assume that the rows of
the picture need to be straightened out. The code below "rotates" each row so
that the magenta occurs at the right hand side of the image. The static turns
into a picture of the word "romance".
"""

import webbrowser
from io import BytesIO

import requests
from PIL import Image

IMG_URL = r'http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif'
URL = r'http://huge:file@www.pythonchallenge.com/pc/return/%s.html'


def main():
    response = requests.get(IMG_URL)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB")
    image_pixels = image.load()
    magenta = (255, 0, 255)

    width, height = image.size
    for rowidx in range(height):
        row = [image_pixels[i, rowidx] for i in range(width)]
        magenta_loc = row.index(magenta)
        row = row[magenta_loc:] + row[:magenta_loc]
        for i, pixel in enumerate(row):
            image_pixels[i, rowidx] = pixel

    image.show()
    webbrowser.open(URL % 'romance')


if __name__ == '__main__':
    main()
