def up_array(arr):
    
    for a in arr:
        if a <0 or a > 9:
            return None
    else:
        if arr == []:
            return None    
        

    ls = [int(x) for x in str(int(''.join(map(str, arr))) + 1)]
    if len(arr) > len(ls):
        for a in range(len(arr) - len(ls)):
            ls.insert(0,0)
    
    return ls  



print(up_array([]))     