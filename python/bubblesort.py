#https://www.codewars.com/kata/56b97b776ffcea598a0006f2

def bubblesort_once(l):
    bubble = l.copy()
    
    for n, num  in enumerate(bubble ):
        if n == len(bubble )-1:
            break
        if num > bubble[n+1]: bubble[n+1], bubble[n] = num, bubble[n+1]
    
    return bubble                 