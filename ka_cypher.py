#https://www.codewars.com/kata/5934d648d95386bc8200010b/train/python

def ka_co_ka_de_ka_me(word):
    
    vowel = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_word = ''
    check = 0
    new_word = str()
    for l in word:
        if l in vowel:
            check = 1
            new_word += l
        
        else:
            if check == 1:
                new_word += 'ka' + l 
                check = 0
            else:    
                new_word += l    
            
    return 'ka' + new_word


print(ka_co_ka_de_ka_me('Abbaa'))