#https://www.codewars.com/kata/55a3cb91d1c9ecaa2900001b
from functools import reduce
def strong_enough(earthquake, age):
    
    return "Safe!" if reduce(lambda a, b: a*b, [sum(x) for x in earthquake]) <= 1000*0.99**age else "Needs Reinforcement!"
