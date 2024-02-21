#https://www.codewars.com/kata/550554fd08b86f84fe000a58

def in_array(array1, array2):
    
    array3 = []
    
    for a in array1:
        for b in array2:
            if a in b: array3.append(a)
    
    return sorted(list(set(array3)))