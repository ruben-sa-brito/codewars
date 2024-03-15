#https://www.codewars.com/kata/5660aa6fa60f03856c000045
def get_honor_path(honor_score, target_honor_score):
    katas = {'2kyus':0, '1kyus':0}
    
    target = target_honor_score - honor_score
    
    if target <= 0: return {}
    
    while True:
        if katas['2kyus'] + katas['1kyus']*2 == target: return katas
        
        if katas['1kyus']*2 + 2 <= target:
            katas['1kyus'] += 1
        else:
            katas['2kyus'] += 1         