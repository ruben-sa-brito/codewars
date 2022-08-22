#https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):

    list1 = []

    for a in recipe:
        if a in available:
            list1.append(int(available[a]/recipe[a])) 

    if len(recipe) == len(list1):
        return min(list1)
    else:
        return 0    

       
    
  
     