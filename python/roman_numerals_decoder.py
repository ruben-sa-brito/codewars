#https://www.codewars.com/kata/51b6249c4612257ac0000005
def solution(roman):
    roman_numbers = {"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    control = 0
    sum = 0
    for num in roman[::-1]:
        sum+= roman_numbers[num] if roman_numbers[num] >= control else roman_numbers[num]*-1
        control = roman_numbers[num]
        
    return sum