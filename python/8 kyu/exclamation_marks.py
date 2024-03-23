#https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
def replace_exclamation(st):
    return ''.join(map(lambda x: '!' if x in 'aeiouAEIOU' else x, st))