#https://www.codewars.com/kata/592edfda5be407b9640000b2
def decode(code, key):
    key = str(key)
    control = 0
    word = str()
    for num in code:
        try:
            word += chr((num-int(key[control]))+96)
            control += 1
        except:
            control = 0
            word += chr((num-int(key[control]))+96)
            control += 1    
        
            
    return word       