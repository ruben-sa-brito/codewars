#https://www.codewars.com/kata/64b6722493f1050058dc3f98
import re
def remove_parentheses(s):
    s = s.replace('()','1y')
    t = re.findall('[0-9,y]+', s)
    for p in t:
        temp = p.split('y')
        temp = filter(lambda x: x!='', temp)
        s = s.replace(p, str(sum([int(n) for n in temp])) +'y')
        
    t = re.findall('\([0-9]+y\)', s)
    
    for p in t:
        temp = p.replace('y','')
        s = s.replace(p, str(int(temp[1:-1])*2)+'y')
    return s 


def eval_parentheses(s):
    while True:
        removed = remove_parentheses(s)
        if removed.count(')') > 0 or removed.count('y') > 1:
            s = remove_parentheses(s)  
        else:
            return int(removed[:-1])