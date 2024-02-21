#https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
def validate_battlefield(field):
    
    ships = {4:0, 3:0, 2:0, 1:0 }
    
    
    for i, line in enumerate(field):
        
        for j, element in enumerate(line):
            
            if element == 1:
                
                if validate_colision(field, i, j):
                    pass
                else:
                    return False 
     
    ship = 0 
    for i, line in enumerate(field):
        
        for j, element in enumerate(line):
            if element == 0 or j==9:
                control = True
                if element ==1 and j ==9 :
                    try:
                        if ship+1 != 1: ships[ship+1] += 1
                    except:
                        return False
                    control = False   
                if ship > 1 and control:
                    if element == 1:
                        try:
                            ships[ship+1] += 1
                        except:
                            return False
                    else:
                        try:
                            
                            ships[ship] += 1
                        except:
                            return False
                    control = True    
                elif ship == 1 or element == 1:
                    if element == 1:
                        
                        if i == 0:
                            if j == 0:
                                if field[i+1][j] == 0:
                                    
                                    ships[1]+=1
                            else:
                                if field[i+1][j] == 0 and field[i+1][j-1] == 0 and field[i][j-1]==0:
                                    ships[1]+=1
                                        
                            
                        elif i == 9:
                            if field[i-1][j] == 0 and field[i][j-1] == 0:
                                
                                ships[1]+=1
                            
                        else:
                            if field[i-1][j] == 0 and field[i+1][j] == 0 and field[i][j-1]==0:
                                
                                ships[1]+=1
                    else:
                        if i == 0:
                            if field[i+1][j-1] == 0:
                                ships[1]+=1
                            
                        elif i == 9:
                            if field[i-1][j-1]==0:
                                ships[1]+=1
                            
                        else:
                            if field[i-1][j-1] == 0 and field[i+1][j-1] == 0:
                                ships[1]+=1                   
                        
                ship = 0        
            elif element == 1:
                ship += 1              
                                
                
                               
    #reversing rows and columns
    field_t = [[x[j] for x in field] for j in range(len(field))] 
    
    for line in field_t:
        for j, element in enumerate(line):
            if element == 0 or j==9:
                control = True
                if element ==1 and j ==9 :
                    try:
                        if ship+1 != 1: ships[ship+1] += 1
                    except:
                            
                            return False 
                    control = False    
                if ship > 1 and control:
                    if element == 1:
                        try:
                            ships[ship+1] += 1
                        except:
                            
                            return False
                    else:
                        try:
                            
                            ships[ship] += 1
                        except:
                            
                            return False
                    control = False        
                ship = 0        
            elif element == 1:
                ship += 1
            
    if ships[4] == 1 and ships[3] == 2 and ships[2] == 3 and ships[1]== 4:
        return True
    else:
        
        return False                           
                
                        



def validate_colision(field, i, j):
    positions = [[1,1],[1,-1],[-1,1],[-1,-1]]
    positions_colision = [[0,1],[0,-1],[-1,0],[1,0]]
    colision = 0
    
    for position in positions:
        try:
            if i+position[0]== -1 or j+position[1] == -1:
                pass
            else:
                if field[i+position[0]][j+position[1]] == 1: 
                    
                    return False
        except:
            pass
    
    for position in positions_colision:
        try:
            
            colision += field[i+position[0]][j+position[1]]
        except:
            pass
        
        if colision >2:
            
            return False  
        
        colision = 0 
        
    return True                       