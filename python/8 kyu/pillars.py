#https://www.codewars.com/kata/5bb0c58f484fcd170700063d
def pillars(num_pill, dist, width):
    return max(((num_pill-1) * dist)*100 + (width*(num_pill-2)), 0)