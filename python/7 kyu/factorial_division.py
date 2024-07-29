#https://www.codewars.com/kata/52f3a8e1f85fadcdf7001e31
from functools import reduce
def factorial_division(n, d):
    
    return  reduce(lambda x, y: x*y, [x for x in range(d+1, n+1)])