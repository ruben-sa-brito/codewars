#https://www.codewars.com/kata/56b8b0ae1d36bb86b2000eaa
from datetime import datetime

def convert(time):
    return time.strftime("%H:%M:%S,%f")[:-3] 
