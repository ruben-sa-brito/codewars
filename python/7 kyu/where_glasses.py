import re
def find_glasses(lst):
    for thing in lst:
        if re.findall(r'O(-)\1*O', thing): return lst.index(thing)