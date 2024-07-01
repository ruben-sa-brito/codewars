#https://www.codewars.com/kata/5a33ec23ee1aaebecf000130
def count_feelings(st, arr):
    feelings = arr.copy()
    
    for word in arr:
        temp = st
        for chr in word:
            if chr not in temp: 
                feelings.remove(word)
                break
            temp = temp.replace(chr, "", 1)
            
    total_feel = len(feelings)
    if total_feel == 1: return f"{total_feel} feeling." 
    return f"{total_feel} feelings."