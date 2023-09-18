#https://www.codewars.com/kata/57f8ff867a28db569e000c4a
def kebabize(st):
    kebab_case = ''.join(['-' + x.lower() if x.isupper() else x for x in st if x.isalpha()])
    if kebab_case:
        if kebab_case[0] == '-': return kebab_case[1:] 
    
    return kebab_case