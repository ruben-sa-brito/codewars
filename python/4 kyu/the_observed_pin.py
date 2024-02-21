#https://www.codewars.com/kata/5263c6999e0f40dee200059d
import itertools 

def get_pins(observed):
    psb_num = []
    contr = {'1':'124', '2':'1235', '3':'236', '4': '1457', '5':'24568', '6':'3569', '7':'478', '8':'57890', '9':'689', '0':'08' }
    for n in observed:
        psb_num.append(contr[n])
      
    
    return [''.join(a) for a in itertools.product(*psb_num)] 
            



    

