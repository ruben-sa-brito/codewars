#https://www.codewars.com/kata/647518391e258e80eedf6e06

def create_two_sets_of_equal_sum(n):
    
    numbers = [x for x in range(1,n+1)]
    
    
    if len(numbers) % 4 == 3:
        del numbers[0:3]
        
    elif len(numbers) % 4 != 0 : return []    
        
    
    half = list()
    
    while len(numbers) != len(half):
        
        half.append(numbers.pop(0))
        half.append(numbers.pop(-1))
    
    if 1 not in half:
        half.append(1), half.append(2), numbers.append(3)    
        
    return numbers, half 
