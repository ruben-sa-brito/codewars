#https://www.codewars.com/kata/5a8bcd980025e99381000099
def square_up(n):
    square = list()
    zeros =  [0 for x in range(n)]
    
    for x in range(n):
        zeros[-(x+1)] = x+1
        
        square += zeros
        
    return square    