#https://www.codewars.com/kata/58a6ac309b5762b7aa000030
def circle_slash(n):
    
    circle = [x+1 for x in range(n)] 
    if n == 0:
        return 0 
    
    while True:
        circle2 = circle.copy()
        
        circle = [x for x in circle if circle.index(x) % 2 == 0]
        
                
        if len(circle) == 1:
            break
        
        if len(circle2) % 2 != 0:
            circle.pop(0)
            

    return circle[0]                