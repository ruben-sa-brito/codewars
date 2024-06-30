#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    if len(s) % 2 != 0: s = s + '_' 

    return [s[x-1:x+1] for x in range(1,  len(s), 2)]     