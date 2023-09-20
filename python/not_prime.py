#https://www.codewars.com/kata/58844f1a76933b1cd0000023
def kill_kth_bit(n, k):
    binary = bin(n)
    
    try:
        
        1/int(binary[-k]) 
        
        if 1-k != 0: binary = binary[0:-k] + '0' + binary[1-k:]
        else: binary = binary[0:-k] + '0'  
        
        return int(binary,2)
    
    except:
        return n    