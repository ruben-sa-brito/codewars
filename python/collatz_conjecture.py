#https://www.codewars.com/kata/577a6e90d48e51c55e000217
def hotpo(n):
    if n == 1: return 0
    def pack(n):
        if n/2 == 1.0: return 1
        elif n %2 == 0: num = n/2    
        else: num = 3*n + 1
        
        return [num, pack(num)]


    def unpack(ls):
        
        if ls[1] == 1:
            return [2,1]
        return ls[0], *unpack(ls[1])
    
    return len(unpack(pack(n)))              
       