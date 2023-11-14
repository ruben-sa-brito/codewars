#https://www.codewars.com/kata/5b02ae6aa2afd8f1b4001ba4
def get_chance(n, x, a):
    chance = (n-x)/n
    
    for drink in range(1,a):
        chance *= ((n-x) - drink) / (n-drink)
        
    return  round(chance, 2)