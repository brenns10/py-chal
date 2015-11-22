#!/usr/bin/env python3
"""
Solution to Python Challenge #12.

Start: http://www.pythonchallenge.com/pc/return/evil.html

This challenge is impressively cool.  The landing page shows an image of
somebody dealing cards into 5 piles.  The image is evil1.jpg.  That seems to
raise the question, what about evil2.jpg?  So you go there, and you find that
the image says "not jpg, gfx".  So you go to evil2.gfx, and you get this
bizzare binary function.  Who knows what you're supposed to do with that,
right?

I Googled around a bit to see if I could find anything about the GFX file
format.  Then I decided there was nothing useful, and I opened the bytes in
Python.  I also opened evil1.jpg's bytes for comparison.  I started to notice
similar bytes, but in weird places.  I looked up the JPG/JFIF wikipedia page
and noticed that these bytes were part of the header.  They were correctly used
in evil1.jpg, but they were repeated and spaced out in evil2.gfx.

Then it hit me.  The bytes are "dealt" just like the cards.  So I indexed by 5
(bytes[::5]) and opened the result with PIL - an image that said dis.
Similarly for the next "hand" (bytes[1::5]).  I got 5 total images (although
number 4 is a bit wonky and truncated).  What a bizzare and fascinating puzzle.

Image 4 (index 3) is PNG, and it is truncated.  If you dump it to a file,
normal image viewers can open it and see "halfway" through the file.  However,
PIL chokes on it and can't display it.

The images spell out "disproportionality", but ity is struck out, so the clue
is "disproportional".
"""

import webbrowser
from io import BytesIO

import requests
from PIL import Image

IMG_URL = r'http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx'
URL = r'http://huge:file@www.pythonchallenge.com/pc/return/%s.html'


def try_show(b):
    try:
        Image.open(BytesIO(b)).show()
    except:
        pass


def main():
    response = requests.get(IMG_URL)

    try_show(response.content[0::5])
    try_show(response.content[1::5])
    try_show(response.content[2::5])
    try_show(response.content[3::5])
    try_show(response.content[4::5])

    webbrowser.open(URL % 'disproportional')


if __name__ == '__main__':
    main()
