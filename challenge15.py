#!/usr/bin/env python3
"""
Solution to Python Challenge #15.
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
