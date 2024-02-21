#https://www.codewars.com/kata/59daf400beec9780a9000045/solutions/python
def name_in_str(strng : str, name : str) -> bool:
    name = [letra.lower() for letra in name]
    for l in strng.lower():
        if l == name[0]: name.remove(l)
        if len(name) == 0: return True
    return False