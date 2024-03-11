#https://www.codewars.com/kata/65c0161a2380ae78052e5731
def stone_pick(arr):
    materials = {"Cobblestone": 0, "Sticks": 0, "Wood": 0}
    
    for material in arr:
        try:
            materials[f"{material}"] += 1
        except:
            pass    
    
    materials["Sticks"] += materials["Wood"] * 4
    
    return min([materials["Cobblestone"]//3, materials["Sticks"]//2])    