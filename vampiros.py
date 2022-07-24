import math

while True:    
    ev1, ev2, at, d =[int(x) for x in input().split(' ')]

    if ev1 == 0 and ev2 == 0  and at == 0 and d == 0:
        break 
    
    r1 = math.ceil(ev1/d)
    r2 = math.ceil(ev2/d)
   
    
    if at == 3:
        prob = 100* (r1/(r2 + r1))
        print('{:.1f}'.format(prob))
    else:
        p = at/6
        prob =100*  ((((1-p)/p)**r1)-1)  /  ((((1-p)/p)**(r1+r2))-1)
        print('{:.1f}'.format(prob))