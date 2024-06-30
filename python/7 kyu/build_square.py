#https://www.codewars.com/kata/59a96d71dbe3b06c0200009c
def generate_shape(n):
    return ''.join(['+'*n+'\n' for x in range(n)])[:-1]