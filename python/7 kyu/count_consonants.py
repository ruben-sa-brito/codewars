#https://www.codewars.com/kata/564e7fc20f0b53eb02000106
def consonant_count(s):
    
    invalid_character = ['a','e','i','o','u',' ']
    return len([x for x in s.lower() if x not in invalid_character and x.isalpha()])