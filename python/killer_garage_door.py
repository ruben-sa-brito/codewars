#https://www.codewars.com/kata/58b1ae711fcffa34090000ea

def controller(events):
    out = str()
    position = '0'
    play = False
    reverse = False
    for sec in events:
        if sec == 'P':
            if play:
                play = False
                
            else:    
                play = True
        
        if sec == 'O':
           if reverse:
               reverse = False
           else: 
               reverse = True 
        
        if play:
            if reverse:
                if int(position) > 0:
                    position = str(int(position) - 1)
                if int(position) == 0:
                    play = False 
                    reverse = False     
                
            
            else:    
                if int(position) <5:
                    position = str(int(position) + 1)
                if int(position) == 5:
                    play = False 
                    reverse = True     
                
            
            out += position
        else:
            out += position    
    
    return out
                              
              
            