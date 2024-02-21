#https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036
def to_csv_text(array):
    return '\n'.join([', '.join(map(str, arr)) for arr in array])    
