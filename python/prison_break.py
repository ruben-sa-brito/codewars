#https://www.codewars.com/kata/6507e3170b7009117e0c7865

def freed_prisoners(prison):
    open, freed = True, 1
    
    if not prison[0]:
        return 0
    
    for x in prison[1:]:
        if x != open:
            freed += 1
            open = not open
            
    return freed           