#https://www.codewars.com/kata/5a331ea7ee1aae8f24000175
color = set("RGB")


def triangle_82(row):
    x=1
    while x !=0:
        row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[9:]))
        if len(row)< 10:
            x = 0
    if len(row) == 1:
        return row    
    else:
        return triangle_simple(row)

def triangle_730(row):
    x=1
    while x !=0:
            row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[81:]))
            if len(row)< 82:
                x = 0
    if len(row) == 1:
        return row
    elif len(row) < 10:
        return triangle_simple(row)    
    else:
        return triangle_82(row)

def triangle_6562(row):
    x=1
    while x !=0:
            row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[729:]))
            if len(row)< 730:
                x = 0
    if len(row) == 1:
        return row
    elif len(row) < 10:
        return triangle_simple(row) 
    elif len(row)< 82:
        return triangle_82(row)    
    else:
        return triangle_730(row)

def triangle_19684(row):
    x=1
    while x !=0:
            row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[6561:]))
            if len(row)< 6562:
                x = 0
    if len(row) == 1:
        return row
    elif len(row) < 10:
        return triangle_simple(row) 
    elif len(row)< 82:
        return triangle_82(row)
    elif len(row)< 730:
        return triangle_730(row)    
    else:
        return triangle_6562(row)                  

def triangle_simple(row):
    while len(row)>1:
        row = ''.join( a if a==b else (color-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row

def triangle(row):
    print(len(row))
    if len(row)<10:
        return triangle_simple(row)
    
    if len(row)<82:
        return triangle_82(row)
    
    if len(row)<730:
        return triangle_730(row)
    
    if len(row)<10000:
        return triangle_6562(row)
    
    if len(row)<100000:
        return triangle_19684(row) 


                      