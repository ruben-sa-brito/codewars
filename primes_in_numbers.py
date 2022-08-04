#https://www.codewars.com/kata/54d512e62a5e54c96200019e

def prime_factors(n):

    prime = 2     
    prime2 = n
    list_fac = []
    cont = 1
    
    while cont !=0:
        if prime2 % prime == 0:
            prime2 = prime2/prime
            if prime == n:
                return f'({n})'
            list_fac.append(prime)
        else:
            prime +=1    
        if prime2 == 1:
            cont = 0

    prim = list(set(list_fac))
    prim.sort()
    factores = ''

    for i in prim:
        if list_fac.count(i)== 1:
            factores += f'({i})'
        else:
            factores += f'({i}**{list_fac.count(i)})'
                
    return factores  

