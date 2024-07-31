# https://www.codewars.com/kata/5208f99aee097e6552000148
def solution(s):
    position = 0
    start = 0
    break_camel = str()
    while position < len(s):
        if s[position].isupper(): 
            break_camel += s[start:position] + ' '
            start = position
        position += 1
    break_camel += s[start:]
    return break_camel