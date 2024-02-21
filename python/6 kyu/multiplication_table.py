#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08

def multiplication_table(size):
    
    base = [item for item in range(1,size+1)]
    prod = list()
    mult = 1
    
    for x in base:
        prod.append([item*mult for item in base])
        mult+=1
        
    return prod