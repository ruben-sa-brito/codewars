#https://www.codewars.com/kata/599db0a227ca9f294b0000c8
def test(r):
    
    scores = {'h':0, 'a':0, 'l':0}
    
    for mark in r:
        if mark >= 9:
            scores['h']+=1
        elif mark >= 7:
            scores['a']+=1
        else:
            scores['l']+=1
               
    media = round((sum(r)/len(r)), 3)
    
    if scores['a'] == 0 and scores['l'] == 0: return [media, scores, 'They did well']
    
    return [media, scores]          