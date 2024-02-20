#https://www.codewars.com/kata/6397b0d461067e0030d1315e
def to_industrial(time):
    if isinstance(time, int): return round(time/60, 2)

    time = time.split(':')
    
    return int(time[0]) + round(int(time[1])/60, 2)



def to_normal(time):
    time_split = str(time).split('.')
    time_split2 =str(time*100).split('.')
    
    minutes = round(float(time_split2[0][-2:] +'.'+ time_split2[1])*0.6)
    
    if minutes == 60: return str((int(time_split[0]) + 1)) + ':00' 
    if minutes <=10 : minutes = '0' + str(minutes)
    return time_split[0] +':'+ str(minutes)


print(to_normal(1.75))
    