#https://www.codewars.com/kata/6512b3775bf8500baea77663
def gimme_the_letters(sp):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = letters + letters.upper()
    if sp[0] == sp[-1] : return sp[0]
    else: return letters[letters.index(sp[0]) : letters.index(sp[-1])] + sp[-1]