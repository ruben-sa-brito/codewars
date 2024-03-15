#https://www.codewars.com/kata/58aa8698ae929e1c830001c7
def find_the_missing_tree(trees):
    trees_set = set(trees)
    trees_dict = {num:trees.count(num) for num in trees_set}
        
    dif = min(trees_dict.values())
    
    for k in trees_dict:
        if trees_dict[k] == dif: return k