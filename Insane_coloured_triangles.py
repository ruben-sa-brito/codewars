#https://www.codewars.com/kata/5a331ea7ee1aae8f24000175
color = set("RGB")


def triangle_100(row):
    x=1
    while x !=0:
        row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[10:]))
        if len(row)<= 10:
            x = 0
    if len(row) == 1:
        return row    
    else:
        return triangle_simple(row)

def triangle_1000(row):
    x=1
    while x !=0:
            row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[99:]))
            if len(row)<= 100:
                x = 0
    if len(row) == 1:
        return row    
    else:
        return triangle_100(row)

def triangle_10000(row):
    x=1
    while x !=0:
            row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[999:]))
            if len(row)<= 1000:
                x = 0
    if len(row) == 1:
        return row    
    else:
        return triangle_1000(row)             

def triangle_simple(row):
    while len(row)>1:
        row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row

def triangle(row):
    if len(row)<100:
        return triangle_100(row)
    
    if len(row)<1000:
        return triangle_1000(row)
    
    if len(row)<10000:
        return triangle_10000(row) 
                       