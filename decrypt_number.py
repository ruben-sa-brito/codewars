#https://www.codewars.com/kata/58a3cb34623e8c119d0000d5

def decrypt(s):
    nm = -1
    
    ctr = 0
    list1 = list()
    list1.append(int(s[-1]))
    nm2 = int(s[-1])
    
    for n in s:
        if nm + len(s) == 0:
            break
        
        if int(s[nm-1]) - (nm2) < 0:
            nm2 = (int(s[nm-1])-ctr)+10 - nm2
            list1.append(nm2)
            
            ctr = 1
        elif(int(s[nm-1]) - (nm2)) == 0 and ctr == 1:
            nm2 = (int(s[nm-1])-ctr)+10 - nm2
            list1.append(nm2)
            
            ctr = 1     
        else:
            nm2 = (int(s[nm-1])-ctr) - nm2
            list1.append(nm2)
            
            ctr = 0
        nm -= 1    
    result = ''
    list1.reverse()
    
    for n in list1 :
        result += str(n)
        
       
    if result[0] == '0':
        return 'impossible'
            
    
    return result    