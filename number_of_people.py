#https://www.codewars.com/kata/5648b12ce68d9daa6b000099


def number(bus_stops):

    numerodepessoas = 0
    
    for entrada, saida in bus_stops:
        numerodepessoas += entrada - saida
    
    return numerodepessoas