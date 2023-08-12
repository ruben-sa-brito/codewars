#https://www.codewars.com/kata/5286b2e162056fd0cb000c20

def calc_next(num):
    
    return num/2 if num%2 ==0 else 3*num +1

def collatz(n):
    if n == 1: return '1'
    seq = str(n) + '->'
    while True:
        seq += str(int((calc_next(n))))
        
        
        if calc_next(n) == 1:
            return seq
        else:
            seq += '->'
            n = calc_next(n)