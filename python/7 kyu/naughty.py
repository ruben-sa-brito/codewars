#https://www.codewars.com/kata/5662b14e0a1fb8320a00005c
def naughty_or_nice(data):
    elements = list()
    for mounth in data:
        elements += data[mounth].values()
    
    if elements.count("Naughty") > elements.count("Nice"):
        return "Naughty!"
    
    return "Nice!"