#https://www.codewars.com/kata/5263c6999e0f40dee200059d
import itertools 

def get_pins(observed):
    psb_num = []
    for n in observed:
        print(n)
        if n == '1':
            psb_num.append('124')
        elif n == '2':
            psb_num.append('1235')
        elif n == '3':
            psb_num.append('236')
        elif n == '4':
            psb_num.append('1457')
        elif n == '5':
            psb_num.append('24568') 
        elif n == '6':
            psb_num.append('3569')
        elif n == '7':
            psb_num.append('478')
        elif n == '8':
            psb_num.append('57890')
        elif n == '9':
            psb_num.append('689')
        elif n == '0':
            psb_num.append('08')
    
    return [''.join(a) for a in itertools.product(*psb_num)] 
            



    



