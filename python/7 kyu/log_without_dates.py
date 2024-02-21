#https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6
from datetime import datetime


def check_logs(log):
    dias = 0
    try:
        hora_ant = datetime.strptime(log[0], '%H:%M:%S')
    except:
        return 0    
    for hour in log:
        
        hora = datetime.strptime(hour, '%H:%M:%S')
        if hora <= hora_ant:
            dias +=1
        hora_ant = hora
                
        
    return dias