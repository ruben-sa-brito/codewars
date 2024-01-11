#https://www.codewars.com/kata/5829994cd04efd4373000468
def name_file(fmt, nbr, start):
    
    if nbr <= 0 or not isinstance(nbr, int) or not isinstance(start, int): return []
    
    return [fmt.replace("<index_no>", str(start+num)) for num in range(nbr)]
        
    

