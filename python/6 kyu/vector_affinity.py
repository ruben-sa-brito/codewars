# https://www.codewars.com/kata/5498505a43e0fd83620010a9
def vector_affinity(a, b):
    if a == b: return 1
    affinity_rate = 1/max(len(a),len(b))
    affinity = 1
    
    if len(a) != len(b): affinity -= (abs(len(a)- len(b)) * affinity_rate)
    
    for n in range(min(len(a), len(b))):
        if a[n] != b[n]: affinity -= affinity_rate
        
    return affinity