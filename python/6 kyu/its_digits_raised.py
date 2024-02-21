#https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b): 
    
    numbers = [x+a for x in range(b-a+1)]

    perfect_numbers = list()
    
    for num in numbers:
        sum_num = 0
        
        for ind, digit in enumerate(str(num)):
            
            sum_num += int(digit) ** (ind+1)
            
        if sum_num == num: perfect_numbers.append(sum_num)
            

    return perfect_numbers

