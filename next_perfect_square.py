from math import sqrt
def find_next_square(sq):
    if sqrt(sq) - int(sqrt(sq)) !=0:
        return -1
    else:
        return (sqrt(sq)+1)**2




