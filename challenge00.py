#!/usr/bin/env python3
"""Solution to Python Challenge #0.

Start: http://www.pythonchallenge.com/pc/def/0.html
Hint: try to change the URL address

The picture shows 2^38, which is 2 ** 38 in Python.  Following the hint, we
change the 0 in the URL to the value of 2 ** 38 to find the answer.

"""

import webbrowser


def main():

    url = "http://www.pythonchallenge.com/pc/def/%d.html" % (2 ** 38)
    webbrowser.open(url)


if __name__ == '__main__':
    main()
