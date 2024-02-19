#https://www.codewars.com/kata/63b06ea0c9e1ce000f1e2407
def alphabet(ns):
    base = sorted(set(ns))[:4]
    
    ns.remove(base[0])
    ns.remove(base[1])
    ns.remove(base[0]*base[1])
    
    
    for num in set(ns):
        if (num * base[1]) in ns:
            base [2] = num
            ns.remove(num)
            break
    
    for num in ns:
        if (num * base[2]) in ns:
            return num