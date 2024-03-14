#https://www.codewars.com/kata/5886da134703f125a6000033
def pages_numbering_with_ink(current, number_of_digits):
    numbers = list()
    numbers.append(str(current))
    current += 1
    
    while len(''.join(numbers)) <= number_of_digits:
        numbers.append(str(current))
        current += 1 
    
    return int(numbers[-2])       