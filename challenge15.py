#!/usr/bin/env python3
"""
Solution to Python Challenge #15.

The calendar shows a January with two key features:
1. The year is (probably) four digits, starting with 1 and ending with 6.
2. The 26th is a Monday.

There are also two comments in the page;
1. he ain't the youngest, he is the second
2. todo: buy flowers for tomorrow

We find a list of dates that satisfy the conditions. We find the "second
youngest" date in that list. And then we find the day after. I looked it up in
Wikipedia and found out that Mozart was born on that day. So hey.
"""

import webbrowser
import datetime

URL = 'http://huge:file@www.pythonchallenge.com/pc/return/%s.html'


def main():
    dates = [datetime.date(i, 1, 26) for i in range(1006, 1997, 10)]
    leap_years = [d for d in dates if d.year % 4 == 0]
    candi_dates = [d for d in leap_years if d.weekday() == 0]
    print(candi_dates[-2])
    print('I guess Mozart was born the next day.')
    webbrowser.open(URL % 'mozart')


if __name__ == '__main__':
    main()
