#https://www.codewars.com/kata/59b5896322f6bbe260002aa0
def find_the_secret(f):
    for alpha in filter(lambda x: isinstance(x, str), f.__code__.co_consts):
        if len(alpha) == 32: return alpha