

def cakes(recipe = {"flour": 500, "sugar": 200, "eggs": 1}, available = {"flour": 1200, "sugar": 1200, "eggs": 5}):
    list1 = []
    for a in recipe:
        if a in available:
            
            list1.append(int(available[a]/recipe[a])) 
    if len(recipe) == len(list1):
        return min(list1)
    else:
        return 0    

       
    
print(cakes())   
     