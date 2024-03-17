#https://www.codewars.com/kata/56576f82ab83ee8268000059
def spacey(array):
    no_space = str()
    no_space_list = list()
    
    for word in array:
        no_space+=word
        no_space_list.append(no_space)
        
    return no_space_list    
    
    