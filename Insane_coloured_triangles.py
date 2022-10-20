#https://www.codewars.com/kata/5a331ea7ee1aae8f24000175
def triangle(row):
    listc = ['R','G','B']
    
        
    
    if len(row) == 1:
        return row
    if len(row) % 2 == 0:
        if row[0]==row[-1]:
            return row[0]
        listc.remove(row[-1])
        listc.remove(row[0])
        return listc[0]
    else:
        
        listi = list()
        if row[0] == row[-2]:
            listi.append(row[0])
        else:
            listc.remove(row[-2])
            listc.remove(row[0])
            listi.append(listc[0])
            listc = ['R','G','B']
        
        if row[1] == row[-1]:
            listi.append(row[1])
        else:
            listc.remove(row[-1])
            listc.remove(row[1])
            listi.append(listc[0])
            listc = ['R','G','B']
            
        if listi[0] == listi[1]:
            return listi[0] 
        else:
            listc.remove(listi[0])
            listc.remove(listi[1])
            
            return listc[0]
            
print(triangle('RBRGBRBG'))            
                  
            
            
                
        
        

     