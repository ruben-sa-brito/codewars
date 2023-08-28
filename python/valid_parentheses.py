#https://www.codewars.com/kata/6411b91a5e71b915d237332d    

def valid_parentheses(paren_str):
    num_paren = 0
    for paren in paren_str:
        num_paren = num_paren + 1 if paren == '(' else num_paren - 1
        if num_paren < 0: return False
    
    return num_paren == 0 
                       