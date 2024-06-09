#https://www.codewars.com/kata/6512c786a07f6a000fe7a274
import re
def find_glasses(lst):
    for thing in lst:
        if re.findall(r'O-+O', thing): return lst.index(thing)