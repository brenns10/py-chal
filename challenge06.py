#!/usr/bin/env python3
"""Solution to Python Challenge #6.

Start: http://www.pythonchallenge.com/pc/def/channel.html

The title of this challenge is "now there are pairs", and the depiction is of a
zipper.  This is really unfair, because pairs + zipper = zip()!!  Right?  Wrong!
Instead of the builtin function zip(), this one is all about the zipfile module.
If you request channel.zip, you find an archive with tons of text files, and a
readme.  And what do you know?  They have the same linked list structure as that
other challenge.  So, you iterate through them until you get to the end, when
you see the instructions to put together the comments.  With the help of the
zipfile module doc, you find the getinfo() function, and string together the
comments into a wordart that says "hockey".

But you're not done.  Instead of the answer *just* being hockey, you have to
look at the letters that each block letter are drawn out of -- 'oxygen'.  And
that's the answer.  I had to hardcode that one too, because there's no simple
Python equivalent.

"""

import webbrowser
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import re


def main():
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    con = urlopen(url)
    zf_bytes = con.readall()
    zf_file = BytesIO(zf_bytes)
    zf = ZipFile(zf_file, 'r')
    fn = '%d.txt'
    curr = 90052
    message = b''

    while True:
        message += zf.getinfo(fn % curr).comment

        text = zf.open(fn % curr).read().decode('utf8')
        print(text)
        match = re.search('nothing is (?P<nothing>\d+)', text)
        if match is None:
            break
        curr = int(match.group('nothing'))

    print(message.decode('utf8'))
    webbrowser.open('http://www.pythonchallenge.com/pc/def/oxygen.html')

if __name__ == "__main__":
    main()
