#https://www.codewars.com/kata/5a4331b18f27f2b31f000085
def replace_letters(word):
    const_letters = {'a':'z','e':'d','i':'h','o':'n','u':'t','b':'e','c':'e','d':'e','f':'i','g':'i','h':'i','j':'o','k':'o','l':'o','m':'o','n':'o','p':'u','q':'u','r':'u','s':'u','t':'u','v':'a','w':'a','x':'a','y':'a','z':'a'}
    replaced_word = str()
    for l in word:
        replaced_word += const_letters[l]
        
    return replaced_word