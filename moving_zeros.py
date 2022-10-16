def move_zeros(lst):
    
    listF = lst.copy()
    list0 = list()
    
    for a in lst:
        if a == 0:
            listF.remove(0)
            list0.append(a)   
            
    listF = listF + list0    
    return listF       