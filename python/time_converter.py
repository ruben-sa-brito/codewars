
from datetime import datetime

def convert(time):
    return time.strftime("%H:%M:%S,%f")[:-3] 
