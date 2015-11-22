#!/usr/bin/env python3
"""
Solution to Python Challenge #10.

Start: http://www.pythonchallenge.com/pc/return/bull.html
Hint: what are you looking at?

This challenge asks len(a[30]) = ?, and it contains a link to the following
sequence:

a = [1, 11, 21, 1211, 111221, ...

I'm sad to admit that I Googled the sequence.  I tried to figure a pattern (add
a certain amount, multiply by a certain amount, etc).  I tried different number
bases.  All sorts of things.  It turns out that this is the "look and say"
sequence.  Just look at the above and start reading it.

1 -> one one -> 11 -> two ones -> 21 -> one two, one one -> 1211 -> one one, one
two, two ones -> ...

Woah.
"""

import webbrowser


def look_and_say(n):
    s = str(n)
    prev = s[0]
    count = 1
    new = ''
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            new += str(count) + prev
            prev = c
            count = 1
    new += str(count) + prev
    return int(new)


def look_and_say_sequence(start, num):
    for _ in range(num):
        yield start
        start = look_and_say(start)


def main():
    l = list(look_and_say_sequence(1, 31))
    s = str(l[30])
    length = len(s)
    template = r'http://www.pythonchallenge.com/pc/return/%d.html'
    webbrowser.open(template % length)


if __name__ == '__main__':
    main()
