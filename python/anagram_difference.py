#https://www.codewars.com/kata/5b1b27c8f60e99a467000041
def anagram_difference(w1, w2):
    if len(w1) > len(w2): w1, w2 = w2, w1 
    removed = 0
    for l in set(w1):
        if l in w2:
            if w1.count(l) != w2.count(l):
                removed += abs(w1.count(l) - w2.count(l))
    w3 = w1 + w2
    
    
    
    for l in set(w2).difference(set(w1)) | set(w1).difference(set(w2)):
        removed += w3.count(l) 
                  
                    
    return removed
