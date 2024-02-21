#https://www.codewars.com/kata/54d4c8b08776e4ad92000835

def isPP(n):
    a = 2
    b = 1
    c= 0 
    while a<n:
        b *= a
        c += 1
        if b == n:
            return [a,c]
        if b > n:
            a += 1
            c = 0
            b = 1    

