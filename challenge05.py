#!/usr/bin/env python3
"""Solution to Python Challenge #5.

Start: http://www.pythonchallenge.com/pc/def/peak.html
Hint: pronounce it

This one's a little unfair to people with American accents.  "Peak hell" is
supposed to sound like pickle.  In the page source, there is a link to a file,
banner.p.  That is a pickle file, which you can unpickle and examine.

The pickle contains a list of lists of tuples.  The tuples are (character,
count) pairs, each inner list is a line, and the outer list is a list of lines.
On each line, you output "character" "count" times, and at the end, you have a
pretty-printed link.  Sadly, I can't find a simple way to convert that ASCII art
to a word, so I had to hard-code the solution in.

"""

import webbrowser
import urllib
import urllib.request
import pickle


def main():
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    connection = urllib.request.urlopen(url)
    obj = pickle.load(connection)
    write(obj)
    webbrowser.open('http://www.pythonchallenge.com/pc/def/channel.html')


def write(obj):
    for line_list in obj:
        for character_tuple in line_list:
            print(character_tuple[0] * character_tuple[1], end="")
        print("")


if __name__ == "__main__":
    main()
