def instrumental(word):
    vowel_pairs = {'a':'á', 'o':'ó', 'u':'ú', 'e': 'é', 'i':'í', 'ö':'ő', 'ü':'ű' }
    front_vowel = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    back_vowel = ['a', 'á', 'o', 'ó', 'u', 'ú']

    if word[-1] in front_vowel:
        try:
            return word[:-1] + vowel_pairs[word[-1]] + 'vel'
        except:
            return word  + 'vel'
    if word[-1] in  back_vowel:
        try:
            return word[:-1] + vowel_pairs[word[-1]] + 'val'
        except:
            return word  + 'val'
        
    if word[-2] in front_vowel:
        return word + word[-1] + 'el'
    
    if word[-2] in back_vowel:
        return word + word[-1] + 'al'
    
    if word[-2:] in ('cs','sz','zs'): 
        if word[-3] in front_vowel: return word[:-1] + word[-2] + word[-1] + 'el'
        else:  return word[:-1] + word[-2] + word[-1] + 'al'
    
    if word[-3] in front_vowel: return word + word[-1] + 'el'

    return word + word[-1] + 'al'