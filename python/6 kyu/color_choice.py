# https://www.codewars.com/kata/55be10de92aad5ef28000023
from math import comb
def checkchoose(m, n):
    if m == 1: return 0
    for num in range(1, n):
        if comb(n, num) == m: return num
    return -1