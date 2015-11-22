#!/usr/bin/env python3
"""
Solution to Python Challenge #13.

Start: http://www.pythonchallenge.com/pc/return/disproportional.html

You start out looking at a phone, and the message is "call him".  Now, when I
was going through level 12, I didn't initially look at evil3.jpg and evil4.jpg.
But it turns out that evil3.jpg says "no more evils..." and evil4.jpg is just a
text file saying Bert is evil.

Anyway, with that in mind, the page has a link to a PHP "phonebook" that gives
back an error in XML when you call it.  Eventually, I realized that it was
xml-rpc.  So, I pulled out my xmlrpc.client and got to work.  The phonebook
application has a "phone" method that takes a string.  I started trying
different things (like "evil") and kept getting the message "He is not the
evil".  Finally, I went back and looked at the evil jpgs again and got the hint.
So, I did phone("bert") and it worked.

"""

import webbrowser
from xmlrpc.client import ServerProxy

PHONEBOOK = 'http://www.pythonchallenge.com/pc/phonebook.php'
URL = 'http://huge:file@www.pythonchallenge.com/pc/return/%s.html'


def main():

    server = ServerProxy(PHONEBOOK)
    response = server.phone('Bert')
    word = response.split('-', 1)[1].strip().lower()
    webbrowser.open(URL % word)


if __name__ == '__main__':
    main()
