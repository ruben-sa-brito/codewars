#https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111
def triangle(row):
    strc = str()
    colors = ['B','G','R']
    ctr = 1
    while True:
        if len(row) == 1:
            return row
        for a in row: 
            
            if ctr != 1:
                if a == b:
                    strc += a
                else:    
                    if ctr != 1:
                        colors.remove(a)
                        colors.remove(b)
                        strc += colors[0]
                        colors = ['B', 'G', 'R']
            b = a            
            
            ctr = 0            
        ctr = 1
        row = strc
        if len(strc) > 1:
            strc = str()
        else:
            return strc