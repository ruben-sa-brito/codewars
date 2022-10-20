#https://www.codewars.com/kata/5a331ea7ee1aae8f24000175
COLORS = set("RGB")

def triangle_simple(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row

def triangle(row):
    if len(row)<10:
        return triangle_simple(row)
    
    x= 1
    
    while x !=0:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[9:]))
        if len(row)<= 10:
            x = 0
    
    if len(row) == 1:
        return row    
    else:
        return triangle_simple(row)
                       