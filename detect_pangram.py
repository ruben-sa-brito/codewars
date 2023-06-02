#https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram(s):
    s = ''.join(x for x in s if x.isalpha()).lower()
    
    return True if  len({x for x in s}) == 26 else False
   

