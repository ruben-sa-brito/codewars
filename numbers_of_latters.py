#https://www.codewars.com/kata/599febdc3f64cd21d8000117

def numbers_of_letters(n):
    numbersl = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = list()
      
    numbers.append(''.join([numbersl[int(n)] for n in str(n)]) )
    
    n = numbers[0]
    
    while True:
        if n in numbersl: 
            if len(n) == numbersl.index(n):
                break
            
        n = len(n)
        
        numbers.append(''.join([numbersl[int(n)] for n in str(n)]) )
        
        n = numbers[-1]
    
        
    return numbers    