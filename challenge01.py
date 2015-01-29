#!/usr/bin/env python3
""""Solution to Python Challenge #1.

Start: http://www.pythonchallenge.com/pc/def/map.html
Hint: everybody thinks twice before solving this.

The picture suggests that every character should be incremented by two.
Initially, I tried simply mapping a function that incremented each character
(using ord() and chr()) in the string.  Many of the characters were jumbled,
but I translated enough to see that the problem recommended string.maketrans(),
and from there the solution was straightforward.

"""

import webbrowser


def main():

    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc "\
           "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr "\
           "gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml "\
           "rfc spj."
    url_template = 'http://www.pythonchallenge.com/pc/def/%s.html'

    trans_from = 'abcdefghijklmnopqrstuvwxyz'
    trans_to = 'cdefghijklmnopqrstuvwxyzab'
    translation = str.maketrans(trans_from, trans_to)

    decoded = text.translate(translation)
    print(decoded)

    new_url = url_template % 'map'.translate(translation)
    print(new_url)
    webbrowser.open(new_url)


if __name__ == '__main__':
    main()
