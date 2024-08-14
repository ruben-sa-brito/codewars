# https://www.codewars.com/kata/52fb87703c1351ebd200081f
from math import ceil

def what_century(year):
    suffixes = {'1':'st', '2':'nd', '3':'rd'}
    if year[2:4] == '99':
        sec = str(ceil(int(year) / 100))
        if 11 <= int(sec) <= 13: return sec + 'th'
        try: return sec + suffixes[sec[1]]
        except: return sec + 'th'
    else:
        sec = str(ceil(int(year) / 100))
        if 11 <= int(sec) <= 13: return sec + 'th'
        try: return sec + suffixes[sec[1]]
        except: return sec + 'th'