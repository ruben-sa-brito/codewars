#https://www.codewars.com/kata/57a73e697cb1f31dd70000d2
def chinese_zodiac(year):

    animals = [
        'Rat', 'Ox', 'Tiger', 
        'Rabbit', 'Dragon', 'Snake', 
        'Horse', 'Goat', 'Monkey', 
        'Rooster', 'Dog', 'Pig'
    ]

    elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']

    return elements[((year-194)//2)%5] + ' ' + animals[(year-1924)%12]