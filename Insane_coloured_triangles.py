#https://www.codewars.com/kata/5a331ea7ee1aae8f24000175
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

     