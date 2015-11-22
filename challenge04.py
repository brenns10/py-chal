#!/usr/bin/env python3
"""Solution to Python Challenge #4

Start: http://www.pythonchallenge.com/pc/def/linkedlist.php
Hint (in page source): urllib may help.  DON'T TRY ALL NOTHINGS, since it will
never end.  400 times is more than enough.

As the name implies, this challenge involves a linked list.  The image links to
the same page with 'nothing' as a GET parameter.  This page has a number, and
it's clear that you have to put that number in the 'nothing' parameter and do
another request.  There are a couple bumps in the list.  The first one is a page
that says "Yes. Divide by 2 and continue."  or something like that.  The second
one says something about there being some misleading numbers.

I dealt with the second "bump" by using a regular expression that always
identifies the correct number in the response.  I dealt with the first bump by
checking for 'Yes.' ... when there is no match.

Finally, after a lot of steps along the path, the path terminates at the name of
the next page.

"""

import webbrowser
import urllib
import urllib.request
import re


def main(currentNothing=94485):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d'
    pattern = r'next nothing is (?P<nothing>\d+)'
    curr_nothing = 94485

    for _ in range(400):  # don't go on forever
        connection = urllib.request.urlopen(url % curr_nothing)
        text = connection.read().decode('utf8')
        print(text)
        match = re.search(pattern, text)
        if match is not None:
            curr_nothing = int(match.group('nothing'))
        elif text.startswith('Yes.'):
            # divide by 2 and keep going
            curr_nothing /= 2
        else:
            webbrowser.open('http://www.pythonchallenge.com/pc/def/%s' % text)
            return
    print('I have failed.')


if __name__ == '__main__':
    main()
