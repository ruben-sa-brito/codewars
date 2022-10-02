#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(snail_map):
    cont = 0
    i=0
    j=0
    x =1
    y =1
    ctr = 0
    fn_list = list()
    ctr_list = list()
    ctr_list.append([i,j])
    
    while cont < len(snail_map)**2:
        
        try: 
            fn_list.append(snail_map[i][j])
        except:
            pass    
        if ctr == 0:
            j +=1
            if len(snail_map)-1 == j:
                ctr = +1
                x *=-1
        else:    
            if ctr % 2 == 0:
                j+=x
                if [i,j] in ctr_list:
                    ctr += 1
                    x*=-1
                    j+=x
                    i+=y
                    ctr_list.append([i,j])
                else:    
                    ctr_list.append([i,j])    
                    if len(snail_map)-1 == j or j == 0:
                        ctr = +1
                        x *=-1
            else:
                i+=y
                if [i,j] in ctr_list:
                    ctr += 1
                    y*=-1
                    i+=y
                    j+=x
                    ctr_list.append([i,j])
                    
                else:    
                    ctr_list.append([i,j])    
                    if len(snail_map)-1 == i or i == 0:
                        ctr += 1
                        y*=-1
        cont += 1              
    
    return fn_list                   