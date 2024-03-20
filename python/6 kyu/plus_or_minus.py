#https://www.codewars.com/kata/65f8279c265f42003ffbd931

from itertools import chain
def plus_or_minus(variables, test):
    num = int('1'*(len(variables)+1))
    total_var = len(variables)
    
    if total_var > 1:
        ls = [num] + [10**x for x in range(1, len(variables))]
    else:
        return '-'+variables if test([1]) < 0 else variables  
        
    result = test(ls)
    
    sinals = list()
    if result < 0: 
        result = str(result)[2:]
        for n in result[::-1]:
            if n == '0' or n == '-': sinals.append('+')
            else: sinals.append('-')
    else:
        result = str(result)[1:]
        for n in result[::-1]:
            if n == '0': sinals.append('-')
            else: sinals.append('+')
    
    if sinals[0] == '-':
        return ''.join(chain.from_iterable(zip(sinals, variables)))
    else:
        return ''.join(chain.from_iterable(zip(sinals, variables)))[1:]
            