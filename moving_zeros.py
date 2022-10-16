#https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(lst):
    
    
    for a in lst:
        if a == 0:
            lst.remove(0)
            lst.append(0)   
               
    return lst      