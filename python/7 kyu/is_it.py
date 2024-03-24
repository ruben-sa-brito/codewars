#https://www.codewars.com/kata/57a06b07cf1fa58b2b000252
import re
def is_it_letter(s):
    return  re.search('[a-zA-Z]', s) is not None