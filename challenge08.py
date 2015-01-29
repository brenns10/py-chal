#!/usr/bin/env python3
"""Solution to Python Challenge #8.

Start: http://www.pythonchallenge.com/pc/def/integrity.html
Hint: where is the missing link?

In the page source there is a comment with a username and password, but they are
obfuscated in some way.  The image is of a bee on a flower.  This should remind
you of bz, as in 'busy as a bee'.  This, plus the obfuscation, suggests the
encryption method bz2, which happens to be in the python standard library.
Plus, the HTTP basic auth on the link from the image has the message 'inflate'.

So, use the bz2 module to decompress the strings, and voila!  Username and
password revealed!

"""

import webbrowser
import bz2


def main():
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    username = bz2.decompress(un).decode('utf8')
    password = bz2.decompress(pw).decode('utf8')

    print('Username: ' + username)
    print('Password: ' + password)
    webbrowser.open('http://%s:%s@www.pythonchallenge.com/pc/return/good.html'
                    % (username, password))


if __name__ == '__main__':
    main()
